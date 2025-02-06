import re

def isValid_full_name(full_name: str) -> dict:
    """
    Valida un nombre completo siguiendo reglas básicas.

    Reglas de validación:
      - Debe tener entre 3 y 50 caracteres.
      - Solo puede contener letras (mayúsculas o minúsculas) y espacios.
      - Puede incluir acentos y tildes (Ej: Á, é, ñ, ü).
      - No puede comenzar ni terminar con espacios.
      - No puede contener múltiples espacios seguidos.

    Args:
        full_name (str): El nombre completo a validar.

    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si el nombre es válido.
              - "message": str con un mensaje descriptivo.
    """
    pattern = r'^(?! )(?!.* {2,})[a-zA-ZÀ-ÖØ-öø-ÿ\s]{3,50}(?<! )$'

    if not full_name:
        return {"isValid": False, "message": "El nombre completo no puede estar vacío."}

    if re.match(pattern, full_name):
        return {"isValid": True, "message": "El nombre completo es válido."}
    else:
        return {
            "isValid": False,
            "message": "El nombre completo debe tener entre 3 y 50 caracteres y solo puede contener letras y espacios. No puede comenzar ni terminar con espacios ni contener múltiples espacios seguidos."
        }
