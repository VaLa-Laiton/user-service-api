from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas import user_schema
from app.core import auth
from app.services import user_data_validator_service, user_service

router = APIRouter()

@router.post("/auth/register")
async def auth_register(user: user_schema.UserCreate, request: Request):
    """
    Endpoint para registrar un usuario.

    Realiza las siguientes acciones:
    1. Valida manualmente el objeto recibido mediante `user_data_validator_service`.
    2. Identifica y retorna los campos inválidos en caso de error.
    3. Verifica si el usuario ya existe en la base de datos (por email o phone_number).
    4. Si la validación es exitosa, guarda el usuario en la base de datos.
    5. Genera un JWT para el usuario recién creado.
    6. Devuelve una respuesta JSON con el usuario guardado y el token de acceso.

    Args:
        user (UserCreate): Datos del usuario a registrar.
        request (Request): Objeto de la solicitud entrante.

    Returns:
        JSONResponse: Respuesta HTTP con el resultado de la operación.
    """
    responseMssg = user_data_validator_service.isValid_user_data(user.model_dump())

    # Verificar si hay algún campo inválido
    invalid_fields = {key: value for key, value in responseMssg.items() if not value["isValid"]}
    if invalid_fields:
        # Si hay errores, devuelve un JSONResponse con HTTP 400 (Bad Request)
        return JSONResponse(
            status_code=400,
            content={
                "error": "Datos inválidos",
                "validations": invalid_fields
            }
        )
    
    # Verificar si el usuario ya existe en la base de datos (por email o phone_number)
    existing_user = await user_service.check_user_exists(user.email, user.phone_number)
    if existing_user["exists"]:
        return JSONResponse(
            status_code=400,
            content={
                "error": f"El {existing_user['field']} ya está registrado. Por favor, use otro."
            }
        )
    
    # Guardar el usuario en la base de datos
    saved_user = await user_service.create_user(user.model_dump())

    # Convertir el usuario guardado a un formato compatible con JSON
    json_compatible_saved_user = jsonable_encoder(saved_user)

    # Generar el JWT con el ID del usuario recién creado
    access_token = auth.create_jwt({"user_id": json_compatible_saved_user["user"]["_id"]})

    # Devolver una respuesta con HTTP 201 (Created)
    return JSONResponse(
        status_code=201,
        content={
            "Mensaje": "Usuario registrado exitosamente.",
            "User": json_compatible_saved_user,
            "access_token": access_token  
        }
    )

@router.post("/auth/login")
def auth_login():
    """
    Endpoint para iniciar sesión.

    Returns:
        dict: Mensaje indicando el propósito del endpoint de login.
    """
    return {"Mensaje": "Esta es el end-point para que un usuario inicie sesión"}
