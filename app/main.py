"""
Módulo principal de la aplicación User Service API.

Ubicación:
    - Este módulo se encuentra en 'app/main.py', que actúa como punto de entrada de la API.

Responsabilidades:
    - Inicializar la instancia de FastAPI utilizando parámetros configurables definidos en 'app/config.py'.
    - Configurar el middleware que añade un encabezado HTTP ('X-Process-Time') a cada respuesta, permitiendo la monitorización del tiempo de procesamiento.
    - Incluir routers para organizar y manejar los endpoints de la aplicación:
        • Endpoints generales definidos en 'app/routers/main.py'.
        • Endpoints de autenticación en 'app/routers/auth.py'.
        • Endpoints para la gestión de usuarios en 'app/routers/users.py'.

Diseño y Organización:
    - La aplicación sigue un diseño modular y una separación clara de responsabilidades, facilitando el mantenimiento, la escalabilidad y la integración con herramientas de documentación automática (por ejemplo, Swagger).
    - Otras funcionalidades clave se encuentran distribuidas en:
        • 'app/core/' para procesos centrales (seguridad, autenticación y RBAC).
        • 'app/models/' y 'app/schemas/' para la definición de modelos de datos y validación de solicitudes.
        • 'app/services/' para la lógica de negocio.
        • 'app/db/' para la conexión a la base de datos (MongoDB).
        • 'app/utils/' para funciones auxiliares.
    - Las pruebas unitarias y de integración se ubican en el directorio 'tests/'.
    - La configuración de contenedores y despliegue se gestiona en los archivos Dockerfile y docker-compose.yml'.

Ejemplo de uso:
    Para iniciar la API utilizando Docker, ejecute en la terminal:
    >>> sudo docker compose up --build

Notas:
    - La configuración de la aplicación (nombre, versión y descripción) se obtiene del módulo 'app/config.py'.
    - El middleware añade el encabezado 'X-Process-Time' en cada respuesta para facilitar la monitorización del rendimiento.
    - Se han importado e incluido routers organizados por funcionalidad, permitiendo una mejor escalabilidad y claridad en la gestión de endpoints.
    - La importación de 'auth_middleware' se ha eliminado en este ejemplo, pero se podrá reintroducir en futuras versiones si se requiere funcionalidad adicional de autenticación a nivel de middleware.
"""

from fastapi import FastAPI
from app import config
from app.routers import main_routes, auth_routes, users_routes
from app.middlewares import main_middleware  # Se omite 'auth_middleware' por no utilizarse actualmente.

# Inicialización de la instancia de FastAPI con parámetros de configuración.
app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION,
    description="API para la gestión de usuarios, autenticación y endpoints generales."
)

# Configuración del middleware para añadir el tiempo de procesamiento de la solicitud.
# Este middleware añade un encabezado HTTP 'X-Process-Time' en cada respuesta,
# facilitando la monitorización y optimización del rendimiento.
app.middleware("http")(main_middleware.add_process_time_header)

# Inclusión del router principal.
# Este router gestiona los endpoints básicos y generales de la aplicación, ubicados en 'app/routers/main.py'.
app.include_router(main_routes.router, tags=["General"])

# Inclusión del router de autenticación.
# Este router maneja la autenticación de usuarios (registro, inicio de sesión, validación de tokens),
# y se encuentra en 'app/routers/auth.py'.
app.include_router(auth_routes.router, prefix="/auth", tags=["Autenticación"])

# Inclusión del router de gestión de usuarios.
# Este router proporciona funcionalidades para la administración y gestión de usuarios, ubicado en 'app/routers/users.py'.
app.include_router(users_routes.router, prefix="/users", tags=["Usuarios"])
