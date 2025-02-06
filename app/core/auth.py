import os
import jwt
import pytz
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, Security
from jwt import ExpiredSignatureError, InvalidTokenError

# Cargar variables de entorno desde el archivo .env si existe.
load_dotenv()

# Define la zona horaria deseada
time_zone = pytz.timezone('America/Bogota')

# Claves secretaa para firmar el JWT
# Obtener claves de entorno para JWT con RS256
# Ruta de los archivos PEM
PRIVATE_KEY_PATH = os.path.join(os.path.dirname(__file__), "../../private.pem")
PUBLIC_KEY_PATH = os.path.join(os.path.dirname(__file__), "../../public.pem")

# Leer el contenido de las claves PEM
try:
    with open(PRIVATE_KEY_PATH, "r") as private_file:
        PRIVATE_KEY = private_file.read()
    with open(PUBLIC_KEY_PATH, "r") as public_file:
        PUBLIC_KEY = public_file.read()
except FileNotFoundError:
    raise RuntimeError("Las claves RSA no se encontraron. Asegúrate de generar 'private.pem' y 'public.pem'.")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")  # Algoritmo que se usara para generar el token
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")) # Tiempo durante el cual el token es valido

def create_jwt(data: dict, expires_delta: timedelta = None):
    """
    Genera un token JWT con la información proporcionada usando RS256.

    Args:
        data (dict): Información a incluir en el token (ej. ID de usuario).
        expires_delta (timedelta, optional): Tiempo de expiración del token.

    Returns:
        str: Token JWT generado.
    """
    to_encode = data.copy()
    expire = datetime.now(time_zone) + (expires_delta or timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # Agrega la expiración al payload

    # Firmar con la clave privada
    token = jwt.encode(to_encode, PRIVATE_KEY, algorithm=JWT_ALGORITHM)
    return token

def verify_jwt(token: str):
    """
    Verifica y decodifica un token JWT usando la clave pública.

    Args:
        token (str): Token JWT a verificar.

    Returns:
        dict: Datos decodificados del token si es válido.
    """
    try:
        decoded_token = jwt.decode(token, PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

# Esquema de seguridad para extraer el token del header "Authorization"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def validate_jwt(token: str = Security(oauth2_scheme)):
    """
    Valida un token JWT con RS256, asegurando que sea válido y no haya expirado.

    Args:
        token (str): Token JWT a validar (se obtiene del header "Authorization").

    Returns:
        dict: Datos decodificados del token si es válido.

    Raises:
        HTTPException: Error 401 si el token es inválido o ha expirado.
    """
    try:
        # Decodificar el token usando la clave pública
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
        return payload  # Retorna los datos del usuario dentro del token

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")