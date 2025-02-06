import re

def isValid_password(password: str) -> dict:
    """
    Valida una contraseña según criterios de seguridad.

    Reglas de validación:
      - Debe tener entre 8 y 50 caracteres.
      - Debe contener al menos una letra mayúscula.
      - Debe contener al menos una letra minúscula.
      - Debe contener al menos un número.
      - Debe contener al menos un carácter especial (@#$%^&+=!_*).
    
    Args:
        password (str): La contraseña a validar.

    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si la contraseña es válida.
              - "message": str con un mensaje descriptivo.
    """
    pattern = r'^(?=.*[a-záéíóúüñ])(?=.*[A-ZÁÉÍÓÚÜÑ])(?=.*\d)(?=.*[@#$%^&+=!_*])[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\d@#$%^&+=!_*]{8,50}$'

    if not password:
        return {"isValid": False, "message": "La contraseña no puede estar vacía."}

    if re.match(pattern, password):
        return {"isValid": True, "message": "La contraseña es válida."}
    else:
        return {
            "isValid": False,
            "message": "La contraseña debe tener entre 8 y 50 caracteres, incluir al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (@#$%^&+=!_*)."
        }
