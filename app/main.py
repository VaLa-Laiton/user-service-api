"""
Módulo principal de la aplicación User Service API.

Este módulo inicializa la instancia de FastAPI, configura el middleware
para agregar un encabezado que indica el tiempo de procesamiento de la solicitud,
e incluye los routers responsables de manejar los endpoints principales, de
autenticación y de gestión de usuarios.

La estructura del código sigue los principios de separación de responsabilidades
y modularidad, facilitando su mantenimiento y escalabilidad.
"""

from fastapi import FastAPI
from app.routers import main_routes, auth_routes, users_routes
from app.middlewares import main_middleware, auth_middleware  # auth_middleware importado pero sin uso en este ejemplo

# Inicialización de la instancia de FastAPI.
app = FastAPI()

# Configuración del middleware.
# Este middleware añade un encabezado HTTP a cada respuesta con el tiempo de procesamiento
# de la solicitud, lo cual es útil para la monitorización y optimización del rendimiento.
app.middleware("http")(main_middleware.add_process_time_header)

# Inclusión del router principal.
# Este router gestiona los endpoints básicos y generales de la aplicación.
app.include_router(main_routes.router)

# Inclusión del router de autenticación.
# Este router maneja la autenticación de usuarios, la emisión y validación de tokens (Registro, Login).
app.include_router(auth_routes.router)

# Inclusión del router de gestión de usuarios.
# Este router proporciona funcionalidades relacionadas con los usuarios.
app.include_router(users_routes.router)
