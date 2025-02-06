from app.db.mongodb import db  # Importar la conexión a la base de datos
from app.models.user_model import Users  # Importar el modelo de usuario
from app.core import security  # Hashear contraseñas antes de guardar
from pydantic import ValidationError

async def create_user(user_data: dict):
    """
    Recibe un esquema de usuario, lo valida con el modelo Users y lo guarda en MongoDB.

    Realiza los siguientes pasos:
    1. Valida el esquema del usuario utilizando el modelo Users de Pydantic.
    2. Hashea la contraseña del usuario antes de almacenarla.
    3. Convierte el objeto validado en un diccionario compatible con MongoDB.
    4. Serializa campos específicos (por ejemplo, avatar_url y user_role) para su almacenamiento.
    5. Inserta el usuario en la colección "users" de MongoDB.
    6. Agrega el ID generado por MongoDB al diccionario y filtra los datos para retornar.

    Args:
        user_data (dict): Datos del usuario ya validados en la capa de validación.

    Returns:
        dict: En caso de éxito, retorna un diccionario con la clave "success" en True y los datos del usuario guardado.
              En caso de error, retorna un diccionario con "success" en False y detalles del error.
    """
    try:
        # Validar el esquema del usuario con el modelo Users de Pydantic
        validated_user = Users(**user_data)

        # Hashear la contraseña antes de guardar
        validated_user.password = security.hash_password(validated_user.password)

        # Convertir el objeto validado en un diccionario para MongoDB
        user_dict = validated_user.model_dump()

        # Convertir campos a tipos serializables
        user_dict['avatar_url'] = str(user_dict['avatar_url'])
        user_dict['user_role'] = user_dict['user_role'].value
        
        # Insertar en MongoDB
        new_user = await db["users"].insert_one(user_dict)
        
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
            "avatar_url": user_dict["avatar_url"]
        }

        return {"success": True, "user": filtered_user}

    except ValidationError as e:
        return {"success": False, "error": "Error de validación", "details": e.errors()}

    except Exception as e:
        return {"success": False, "error": "Error al guardar el usuario", "details": str(e)}
