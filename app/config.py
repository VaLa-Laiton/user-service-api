"""
Módulo de Configuración de la aplicación User Service API.

Ubicación:
    - Este módulo se encuentra en 'app/config.py' y centraliza la configuración global de la aplicación.

Responsabilidades:
    - Cargar variables de entorno desde un archivo '.env' utilizando 'python-dotenv'.
    - Definir parámetros generales de la aplicación, tales como el nombre, la versión y el modo de depuración (DEBUG).
    - Configurar la conexión a la base de datos MongoDB a partir de variables de entorno, construyendo la URI de conexión.
    - Establecer la configuración para la autenticación JWT, incluyendo la carga de claves RSA (archivos PEM), algoritmo y tiempo de expiración del token.
    - Configurar la zona horaria de la aplicación utilizando la librería 'pytz'.

Estructura:
    - Se obtienen los valores de configuración mediante 'os.getenv', proporcionando valores por defecto cuando no se encuentran definidos.
    - La conexión a MongoDB se configura mediante una URI que integra usuario, contraseña, host, puerto y nombre de base de datos.
    - Las claves RSA (privada y pública) se cargan desde archivos PEM ubicados en el directorio superior a 'app'.
    - La zona horaria se establece a partir de la variable de entorno 'TIME_ZONE', con un valor por defecto de "America/Bogota".

Notas:
    - Es esencial contar con un archivo '.env' en la raíz del proyecto que contenga las variables necesarias.
    - Si las claves RSA no se encuentran en las rutas especificadas, se lanzará un error en tiempo de ejecución, evitando la continuación de la aplicación sin la configuración de seguridad adecuada.
"""

import os
import pytz
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde un archivo '.env' ubicado en la raíz del proyecto.
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# ---------------------------------
# Configuración General
# ---------------------------------
APP_NAME = os.getenv("APP_NAME", "My FastAPI App")
APP_VERSION = os.getenv("APP_VERSION", "0.1")
# DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ---------------------------------
# Configuración de la Base de Datos (MongoDB)
# ---------------------------------
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
MONGO_DB = os.getenv("MONGO_INITDB_DATABASE", "mydatabase")
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

# ---------------------------------
# Configuración JWT y Claves PEM
# ---------------------------------
# Definir las rutas de las claves PEM, ubicadas en el directorio superior a 'app'.
PRIVATE_KEY_PATH = os.path.join(os.path.dirname(__file__), "../private.pem")
PUBLIC_KEY_PATH = os.path.join(os.path.dirname(__file__), "../public.pem")

# Cargar el contenido de las claves PEM.
try:
    with open(PRIVATE_KEY_PATH, "r") as private_file:
        PRIVATE_KEY = private_file.read()
    with open(PUBLIC_KEY_PATH, "r") as public_file:
        PUBLIC_KEY = public_file.read()
except FileNotFoundError:
    raise RuntimeError("Las claves RSA no se encontraron. Asegúrate de generar 'private.pem' y 'public.pem'.")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "RS256")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# ---------------------------------
# Configuración de Zona Horaria
# ---------------------------------
TIME_ZONE = pytz.timezone(os.getenv("TIME_ZONE", "America/Bogota"))
