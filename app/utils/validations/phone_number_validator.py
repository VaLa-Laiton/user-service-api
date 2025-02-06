from pydantic import BaseModel, PositiveInt, ValidationError

def isValid_phone_number(phone_number: int) -> dict:
    """
    Valida un número de teléfono usando Pydantic.

    Reglas de validación:
      - Debe ser un número entero positivo (sin signos ni caracteres especiales).
      - No puede ser negativo o contener letras.

    Args:
        phone_number (int): Número de teléfono a validar.

    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si el número es válido.
              - "message": str con un mensaje descriptivo.
    """
    class PhoneNumberSchema(BaseModel):
        phone_number: PositiveInt  # Usa Pydantic para validar que sea un número positivo

    try:
        PhoneNumberSchema(phone_number=phone_number)
        return {"isValid": True, "message": "El número de teléfono es válido."}
    except ValidationError:
        return {"isValid": False, "message": "El número de teléfono no es válido. Debe ser un número positivo y sin caracteres especiales."}
