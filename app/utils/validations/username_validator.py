import re

def isValid_username(username: str) -> dict:
    """
    Valida un nombre de usuario usando una expresión regular.
    
    Reglas de validación:
      - Debe tener entre 3 y 50 caracteres.
      - Solo se permiten letras (mayúsculas o minúsculas), números, guiones bajos (_), guiones (-) y puntos (.).
      - No puede comenzar ni terminar con un guion (-), guion bajo (_) o punto (.).
      - No puede contener dos guiones, guiones bajos o puntos seguidos.
    
    Args:
        username (str): El nombre de usuario a validar.
    
    Returns:
        dict: Con dos propiedades:
              - "isValid": bool que indica si la validación fue exitosa.
              - "message": str con un mensaje descriptivo.
    """
    # Patrón mejorado para usernames con letras, números, guion bajo (_), guion (-) y punto (.)
    pattern = r'^(?![-_.])(?!.*[-_.]{2})[a-zA-Z0-9._-]{3,50}(?<![-_.])$'
    
    if not username:
        return {"isValid": False, "message": "El nombre de usuario no puede estar vacío."}
    
    if re.match(pattern, username):
        return {"isValid": True, "message": "El nombre de usuario es válido."}
    else:
        return {
            "isValid": False, 
            "message": "El nombre de usuario debe tener entre 3 y 50 caracteres y solo puede contener letras, números, guion bajo (_), guion (-) y punto (.). No puede comenzar ni terminar con estos símbolos ni tener dos seguidos."
        }
