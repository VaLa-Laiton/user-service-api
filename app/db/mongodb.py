import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import user

# Cargar variables desde .env si existen
load_dotenv()

# Obtener variables de entorno
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
MONGO_DB = os.getenv("MONGO_INITDB_DATABASE", "mydatabase")

# Crear URI de conexión
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

# Crear cliente asíncrono
client = AsyncIOMotorClient(MONGO_URI)

# Seleccionar la base de datos
db = client[MONGO_DB]

# Crear una colección (ejemplo: "users")
collection_name = "users"
collection = db[collection_name]

async def check_connection():
    print(user.Users.holis())
    try:
        # Enviar un comando 'ping' a la base de datos para verificar la conexión
        result = await db.command("ping")
        if result["ok"] == 1.0:
            return("✅ Conexión exitosa a MongoDB")
        else:
            return("⚠️ No se pudo conectar a MongoDB")
    except Exception as e:
        return(f"❌ Error de conexión: {e}")