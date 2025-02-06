from pydantic import BaseModel, EmailStr, ValidationError

def isValid_email(email: str) -> dict:
    """
    Valida una dirección de correo electrónico usando Pydantic v2.

    Reglas de validación:
      - Debe ser un correo válido según el estándar RFC 5322.
      - Debe contener un dominio válido y una estructura correcta.

    Args:
        email (str): El correo electrónico a validar.

    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si el email es válido.
              - "message": str con un mensaje descriptivo.
    """
    class EmailSchema(BaseModel):
        email: EmailStr  # Usa Pydantic para validar el email

    try:
        EmailSchema(email=email)
        return {"isValid": True, "message": "El correo electrónico es válido."}
    except ValidationError:
        return {"isValid": False, "message": "El correo electrónico no es válido. Asegúrate de ingresar una dirección correcta."}
