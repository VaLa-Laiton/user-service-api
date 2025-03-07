from app.db.mongodb import db  # Importar la conexión a la base de datos
from app.models.user_model import User  # Importar el modelo de usuario
from app.core import security  # Hashear contraseñas antes de guardar
from pydantic import ValidationError

async def create_user(user_data: dict):
    """
    Recibe un esquema de usuario, lo valida con el modelo User y lo guarda en MongoDB.

    Realiza los siguientes pasos:
    1. Valida el esquema del usuario utilizando el modelo User de Pydantic.
    2. Hashea la contraseña del usuario antes de almacenarla.
    3. Convierte el objeto validado en un diccionario compatible con MongoDB.
    4. Serializa campos específicos (por ejemplo, avatar_url y user_role) para su almacenamiento.
    5. Inserta el usuario en la colección "user" de MongoDB.
    6. Agrega el ID generado por MongoDB al diccionario y filtra los datos para retornar.

    Args:
        user_data (dict): Datos del usuario ya validados en la capa de validación.

    Returns:
        dict: En caso de éxito, retorna un diccionario con la clave "success" en True y los datos del usuario guardado.
              En caso de error, retorna un diccionario con "success" en False y detalles del error.
    """
    try:
        # Validar el esquema del usuario con el modelo User de Pydantic
        validated_user = User(**user_data)

        # Hashear la contraseña antes de guardar
        validated_user.password = security.hash_password(validated_user.password)

        # Convertir el objeto validado en un diccionario para MongoDB
        user_dict = validated_user.model_dump()

        # Convertir campos a tipos serializables
        user_dict['avatar_url'] = str(user_dict['avatar_url'])
        user_dict['user_role'] = user_dict['user_role'].value
        
        # Insertar en MongoDB
        new_user = await db["user"].insert_one(user_dict)
        
        # Agregar el ID generado por MongoDB al diccionario
        user_dict["_id"] = str(new_user.inserted_id)

        # Filtrar los datos antes de retornar
        filtered_user = {
            "_id": user_dict["_id"],
            "username": user_dict["username"],
            "email": user_dict["email"],
            "phone_number": user_dict["phone_number"],
            "full_name": user_dict["full_name"],
            "password": user_dict["password"],
            "avatar_url": user_dict["avatar_url"],
            "user_role": user_dict["user_role"]
        }

        return {"success": True, "user": filtered_user}

    except ValidationError as e:
        return {"success": False, "error": "Error de validación", "details": e.errors()}

    except Exception as e:
        return {"success": False, "error": "Error al guardar el usuario", "details": str(e)}

async def check_user_exists(email: str, phone_number: int) -> dict:
    """
    Verifica si el email o el número de teléfono ya están registrados en la base de datos.

    Args:
        email (str): Correo electrónico a verificar.
        phone_number (int): Número de teléfono a verificar.

    Returns:
        dict: Diccionario con la siguiente estructura:
            - "exists": True si el usuario ya está registrado, False si no lo está.
            - "field": Indica cuál campo es duplicado ("email" o "phone_number"), o None si no hay coincidencias.
            - "error": (Opcional) Mensaje de error en caso de excepción.
    """
    try:
        # Buscar en la colección "user" si existe un usuario con el email o el número de teléfono proporcionado
        existing_user = await db["user"].find_one(
            {"$or": [{"email": email}, {"phone_number": phone_number}]}
        )

        if existing_user:
            # Determinar qué campo presenta duplicación
            duplicated_field = "email" if existing_user["email"] == email else "phone_number"
            return {"exists": True, "field": duplicated_field}

        # Retornar que no existe duplicado
        return {"exists": False, "field": None}

    except Exception as e:
        # En caso de error, se retorna el mensaje de error junto con exists en False
        return {"exists": False, "error": str(e)}
