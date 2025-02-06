"""
Módulo de conexión a la base de datos MongoDB utilizando Motor (AsyncIOMotorClient).

Este módulo carga las variables de entorno, configura la conexión a MongoDB,
crea un cliente asíncrono y define funciones auxiliares para interactuar con la base de datos.
"""

import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import user_model  # Importación de modelos (asegúrate de utilizarlos según corresponda)

# Cargar variables de entorno desde el archivo .env si existe.
load_dotenv()

# Obtener variables de entorno para la configuración de MongoDB.
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
MONGO_DB = os.getenv("MONGO_INITDB_DATABASE", "mydatabase")

# Construir la URI de conexión a MongoDB.
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

# Crear el cliente asíncrono para MongoDB.
client = AsyncIOMotorClient(MONGO_URI)

# Seleccionar la base de datos.
db = client[MONGO_DB]

# Definir la colección de usuarios.
collection_name = "users"
collection = db[collection_name]

async def check_connection():
    """
    Verifica la conexión a MongoDB enviando un comando 'ping'.

    Returns:
        str: Mensaje indicando si la conexión fue exitosa, fallida o si ocurrió un error.
    """
    try:
        # Enviar el comando 'ping' a la base de datos.
        result = await db.command("ping")
        if result["ok"] == 1.0:
            return "✅ Conexión exitosa a MongoDB"
        else:
            return "⚠️ No se pudo conectar a MongoDB"
    except Exception as e:
        # Retornar un mensaje de error en caso de excepción.
        return f"❌ Error de conexión: {e}"
