from pydantic import BaseModel, AnyUrl, ValidationError

def isValid_avatar_url(avatar_url: str) -> dict:
    """
    Valida una URL de la foto de perfil del usuario usando Pydantic v2.

    Reglas de validación:
      - Debe ser una URL válida con un esquema correcto (http, https).
      - Puede contener dominios, subdominios, rutas y parámetros.

    Args:
        avatar_url (str): La URL de la imagen a validar.

    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si la URL es válida.
              - "message": str con un mensaje descriptivo.
    """
    class AvatarSchema(BaseModel):
        url: AnyUrl  # Usa Pydantic para validar la URL

    try:
        AvatarSchema(url=avatar_url)
        return {"isValid": True, "message": "La URL de la foto de perfil es válida."}
    except ValidationError:
        return {"isValid": False, "message": "La URL de la foto de perfil no es válida. Asegúrate de ingresar una dirección correcta."}
