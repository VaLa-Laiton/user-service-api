"""
Módulo de Conexión a la Base de Datos MongoDB.

Ubicación:
    - Este módulo se encuentra en 'app/db/mongodb.py' y es el responsable de gestionar la conexión asíncrona a MongoDB utilizando Motor (AsyncIOMotorClient).

Responsabilidades:
    - Establecer una conexión asíncrona a MongoDB utilizando los parámetros de conexión definidos en 'app/config.py'.
    - Proveer acceso a la base de datos configurada y definir las colecciones específicas, según lo establecido en el diagrama de entidad-relación:
         • "User" para documentos de usuarios.
         • "Company" para documentos de compañías.
         • "Role" para documentos de roles.
         • "Endpoint" para documentos de endpoints.
         • "Permission" para documentos de permisos.
         • "Subscription" para documentos de suscripciones.
    - Facilitar una función auxiliar, 'check_connection', que verifica la conectividad a la base de datos mediante un comando 'ping', permitiendo diagnosticar problemas de conexión en tiempo de ejecución.
    - Centralizar la configuración de la base de datos para que pueda ser reutilizada en otras partes de la aplicación.

Estructura:
    - Se importa la configuración global desde 'app/config.py' para obtener la URI de conexión (MONGO_URI) y el nombre de la base de datos (MONGO_DB).
    - Se instancia un cliente asíncrono (AsyncIOMotorClient) utilizando la URI de conexión proporcionada.
    - Se obtiene el objeto de la base de datos a partir del nombre definido en la configuración.
    - Se definen las colecciones especificadas en el diagrama de entidad-relación.
    - La función 'check_connection' es asíncrona y envía un comando 'ping' a la base de datos para verificar que la conexión esté operativa.

Notas:
    - Es fundamental que el archivo '.env' esté correctamente configurado y que 'app/config.py' contenga los valores necesarios para la conexión a MongoDB.
    - La función 'check_connection' puede ser invocada en endpoints de monitoreo o durante las pruebas para asegurar la salud de la conexión a la base de datos.
    - El uso de Motor permite aprovechar el modelo asíncrono de FastAPI para manejar múltiples solicitudes concurrentes de manera eficiente.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app import config

# Crear el cliente asíncrono para MongoDB utilizando la URI definida en la configuración.
client = AsyncIOMotorClient(config.MONGO_URI)

# Seleccionar la base de datos utilizando el nombre especificado en la configuración.
db = client[config.MONGO_DB]

# Definir las colecciones de la base de datos.
# Estas variables definen la referencia a cada colección especificada en el diagrama de entidad-relación:
#   - "User" para documentos de usuarios.
#   - "Company" para documentos de compañías.
#   - "Role" para documentos de roles.
#   - "Endpoint" para documentos de endpoints.
#   - "Permission" para documentos de permisos.
#   - "Subscription" para documentos de suscripciones.
user_collection = db["user"]
company_collection = db["company"]
role_collection = db["role"]
endpoint_collection = db["endpoint"]
permission_collection = db["permission"]
subscription_collection = db["subscription"]

async def check_connection():
    """
    Verifica la conexión a MongoDB enviando un comando 'ping'.

    Esta función asíncrona envía un comando 'ping' a la base de datos y evalúa la respuesta
    para determinar si la conexión es exitosa. Es útil para diagnosticar y monitorear la salud
    de la conexión a MongoDB.

    Returns:
        str: Un mensaje que indica el estado de la conexión:
             - "✅ Conexión exitosa a MongoDB" si el comando 'ping' responde correctamente.
             - "⚠️ No se pudo conectar a MongoDB" si la respuesta no indica éxito.
             - Un mensaje de error detallado en caso de excepción.

    Detalles sobre el manejo de excepciones:
        - Se capturan excepciones genéricas (por ejemplo, problemas de red o errores inesperados) durante la operación de 'ping'.
        - Esto facilita la integración con sistemas de logging y simplifica el diagnóstico de errores en entornos de producción.
    """
    try:
        # Enviar el comando 'ping' a la base de datos.
        result = await db.command("ping")
        if result.get("ok") == 1.0:
            return "✅ Conexión exitosa a MongoDB"
        else:
            return "⚠️ No se pudo conectar a MongoDB"
    except Exception as e:
        # Retornar un mensaje de error en caso de que ocurra alguna excepción.
        return f"❌ Error de conexión: {e}"
