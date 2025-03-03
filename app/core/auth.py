"""
Módulo de Gestión y Validación de Tokens JWT.

Ubicación:
    - Este módulo se encuentra en 'app/core/auth.py'
      y es responsable de la creación, verificación y validación de tokens JWT utilizados para la autenticación
      en la aplicación User Service API.

Responsabilidades:
    - Generar tokens JWT firmados con la clave privada utilizando el algoritmo RS256.
    - Verificar y decodificar tokens JWT utilizando la clave pública, asegurando la integridad y autenticidad
      del token.
    - Validar tokens JWT extraídos del encabezado "Authorization" a través del esquema de seguridad OAuth2, facilitando
      la protección de endpoints en la API.

Estructura:
    - Se importa la configuración global desde 'app/config.py', la cual provee:
        • PRIVATE_KEY: Clave privada para firmar tokens.
        • PUBLIC_KEY: Clave pública para verificar tokens.
        • JWT_ALGORITHM: Algoritmo utilizado para la codificación y decodificación (por defecto RS256).
        • JWT_ACCESS_TOKEN_EXPIRE_MINUTES: Tiempo de expiración predeterminado del token (en minutos).
        • TIME_ZONE: Zona horaria utilizada para calcular el tiempo de expiración.
    - Se define un esquema de seguridad OAuth2 (OAuth2PasswordBearer) que extrae el token del header "Authorization"
      utilizando el endpoint '/auth/login'.
    - Se implementan las siguientes funciones:
        • create_jwt(data: dict, expires_delta: timedelta = None): Genera un token JWT que incluye la información
          proporcionada y la fecha de expiración.
        • verify_jwt(token: str): Verifica y decodifica un token JWT, retornando el payload decodificado si el token es válido.
        • validate_jwt(token: str = Security(oauth2_scheme)): Valida el token JWT obtenido del header "Authorization",
          lanzando excepciones HTTP 401 si el token es inválido o ha expirado.

Notas:
    - Es fundamental que las claves RSA (PRIVATE_KEY y PUBLIC_KEY) se hayan configurado correctamente en 'app/config.py'.
    - El manejo de excepciones (lanzando HTTPException con código 401) asegura que se rechacen tokens expirados o inválidos,
      protegiendo así las rutas de acceso no autorizado.
    - La integración con FastAPI y el uso del esquema OAuth2 permiten una validación automática del token en cada solicitud protegida.
"""

import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Security
from jwt import ExpiredSignatureError, InvalidTokenError

# Importar configuraciones desde config.py
from app.config import PRIVATE_KEY, PUBLIC_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES, TIME_ZONE

# Esquema de seguridad para extraer el token del header "Authorization"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_jwt(data: dict, expires_delta: timedelta = None):
    """
    Genera un token JWT firmado con RS256 que contiene la información proporcionada.

    Esta función crea un token JWT a partir de un diccionario de datos (por ejemplo, el identificador
    del usuario u otra información relevante). Se añade una fecha de expiración al token, calculada
    en función de la zona horaria configurada (TIME_ZONE). Si no se especifica un tiempo de expiración,
    se utiliza el valor por defecto definido en JWT_ACCESS_TOKEN_EXPIRE_MINUTES.

    Args:
        data (dict): Información a incluir en el token (por ejemplo, el ID del usuario).
        expires_delta (timedelta, optional): Tiempo de expiración del token. Si se omite, se usa el valor
            por defecto de JWT_ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: Token JWT generado, firmado con la clave privada (PRIVATE_KEY) y utilizando el algoritmo especificado
             en JWT_ALGORITHM.
    """
    to_encode = data.copy()
    expire = datetime.now(TIME_ZONE) + (expires_delta or timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # Agrega la fecha de expiración al payload

    # Firmar y codificar el token con la clave privada
    token = jwt.encode(to_encode, PRIVATE_KEY, algorithm=JWT_ALGORITHM)
    return token

def verify_jwt(token: str):
    """
    Verifica y decodifica un token JWT utilizando la clave pública.

    Esta función decodifica el token JWT proporcionado y valida su integridad y autenticidad utilizando la
    clave pública (PUBLIC_KEY). Si el token es válido, se devuelve el payload decodificado. En caso de que el token
    haya expirado o resulte inválido, se lanza una excepción HTTP con el código 401.

    Args:
        token (str): Token JWT a verificar.

    Returns:
        dict: Datos decodificados del token si la verificación es exitosa.

    Raises:
        HTTPException: Con código 401 y detalle "Token expirado" si el token ha caducado.
        HTTPException: Con código 401 y detalle "Token inválido" si el token no es válido.
    """
    try:
        decoded_token = jwt.decode(token, PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def validate_jwt(token: str = Security(oauth2_scheme)):
    """
    Valida un token JWT obtenido del encabezado "Authorization".

    Esta función se integra con FastAPI mediante el uso del esquema de seguridad OAuth2 para extraer el token JWT
    de la solicitud. Posteriormente, se valida y decodifica el token utilizando la clave pública. Si el token es válido,
    se retornan los datos decodificados; en caso contrario, se lanzan excepciones HTTP que indican si el token ha
    expirado o es inválido.

    Args:
        token (str, opcional): Token JWT a validar, obtenido automáticamente del encabezado "Authorization" gracias
            a la dependencia Security y al esquema oauth2_scheme.

    Returns:
        dict: Datos decodificados del token si este es válido.

    Raises:
        HTTPException: Con código 401 y detalle "Token expirado" si el token ha caducado.
        HTTPException: Con código 401 y detalle "Token inválido" si el token no es válido.
    """
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
        return payload  # Retorna el payload con los datos del usuario contenido en el token
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
