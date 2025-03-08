"""
Módulo de Rutas Principales para la API de User Service.

Ubicación:
    - Este módulo se encuentra en 'app/routers/main_routes.py' y define los endpoints principales de la API.

Responsabilidades:
    - Proveer endpoints de bienvenida y verificación de la conexión a la base de datos (ping).
    - Definir las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para las entidades principales del sistema:
         • User: Gestión de usuarios.
         • Company: Gestión de compañías.
         • Role: Gestión de roles.
         • Endpoint: Gestión de endpoints de la API.
         • Permission: Gestión de permisos asignados a roles sobre endpoints.
         • Subscription: Gestión de suscripciones de compañías.
    - Facilitar la integración y el manejo centralizado de rutas a través de FastAPI, organizándolas bajo un prefijo y etiquetas específicas.

Estructura:
    - Se crea un objeto APIRouter con un prefijo ("/api/user-service") y etiquetas ("User Service API") para agrupar los endpoints.
    - Se definen endpoints de tipo GET para bienvenida y ping.
    - Se implementan endpoints CRUD para cada una de las entidades del sistema, devolviendo modelos Pydantic correspondientes.
    - Cada endpoint incluye una breve descripción y, en algunos casos, una lógica simulada (por ejemplo, levantando HTTPException cuando no se encuentra el recurso).

Notas:
    - La lógica de negocio de cada endpoint está actualmente representada por retornos de ejemplo o excepciones. En una implementación real, se reemplazarán estas secciones con la interacción con la base de datos y la aplicación de la lógica correspondiente.
    - Se utiliza la función 'check_connection' del módulo mongodb para verificar la conectividad a la base de datos.
"""

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.db import mongodb
from typing import List
from app.schemas.user_schema import User
# from app.models.user_model import User as UserModel 
from app.models.company_model import Company
from app.models.role_model import Role
from app.models.endpoint_model import Endpoint
from app.models.permission_model import Permission
from app.models.subscription_model import Subscription

router = APIRouter(prefix="/api/user-service", tags=["User Service API"])

@router.get("/")
def welcome():
    """
    Endpoint de bienvenida.

    Returns:
        dict: Mensaje de bienvenida en formato JSON.
    """
    return {"Mensaje": "Hola, que tal? Bienvenido a user-service-api"}

@router.get("/ping")
async def ping():
    """
    Endpoint para verificar la conexión a la base de datos.

    Returns:
        JSONResponse: Resultado de la verificación de conexión a MongoDB.
    """
    return await mongodb.check_connection()

# -------------------------
# CRUD para la entidad User
# -------------------------
@router.post("/users", response_model=User)
def create_user(user: User):
    # Lógica para crear el usuario
    return user

@router.get("/users", response_model=List[User])
def list_users():
    # Lógica para listar todos los usuarios
    return []

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    # Lógica para obtener un usuario por su id
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    # Lógica para actualizar el usuario
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    # Lógica para eliminar (eliminación lógica o física) el usuario
    return {"message": "User deleted"}

# -----------------------------
# CRUD para la entidad Company
# -----------------------------
@router.post("/companies", response_model=Company)
def create_company(company: Company):
    # Lógica para crear la compañía
    return company

@router.get("/companies", response_model=List[Company])
def list_companies():
    # Lógica para listar todas las compañías
    return []

@router.get("/companies/{company_id}", response_model=Company)
def get_company(company_id: str):
    # Lógica para obtener una compañía por su id
    raise HTTPException(status_code=404, detail="Company not found")

@router.put("/companies/{company_id}", response_model=Company)
def update_company(company_id: str, company: Company):
    # Lógica para actualizar la compañía
    return company

@router.delete("/companies/{company_id}")
def delete_company(company_id: str):
    # Lógica para eliminar la compañía
    return {"message": "Company deleted"}

# --------------------------
# CRUD para la entidad Role
# --------------------------
@router.post("/roles", response_model=Role)
def create_role(role: Role):
    # Lógica para crear el rol
    return role

@router.get("/roles", response_model=List[Role])
def list_roles():
    # Lógica para listar todos los roles
    return []

@router.get("/roles/{role_id}", response_model=Role)
def get_role(role_id: str):
    # Lógica para obtener un rol por su id
    raise HTTPException(status_code=404, detail="Role not found")

@router.put("/roles/{role_id}", response_model=Role)
def update_role(role_id: str, role: Role):
    # Lógica para actualizar el rol
    return role

@router.delete("/roles/{role_id}")
def delete_role(role_id: str):
    # Lógica para eliminar el rol
    return {"message": "Role deleted"}

# -----------------------------
# CRUD para la entidad Endpoint
# -----------------------------
@router.post("/endpoints", response_model=Endpoint)
def create_endpoint(endpoint: Endpoint):
    # Lógica para crear el endpoint
    return endpoint

@router.get("/endpoints", response_model=List[Endpoint])
def list_endpoints():
    # Lógica para listar todos los endpoints
    return []

@router.get("/endpoints/{endpoint_id}", response_model=Endpoint)
def get_endpoint(endpoint_id: str):
    # Lógica para obtener un endpoint por su id
    raise HTTPException(status_code=404, detail="Endpoint not found")

@router.put("/endpoints/{endpoint_id}", response_model=Endpoint)
def update_endpoint(endpoint_id: str, endpoint: Endpoint):
    # Lógica para actualizar el endpoint
    return endpoint

@router.delete("/endpoints/{endpoint_id}")
def delete_endpoint(endpoint_id: str):
    # Lógica para eliminar el endpoint
    return {"message": "Endpoint deleted"}

# -------------------------------
# CRUD para la entidad Permission
# -------------------------------
@router.post("/permissions", response_model=Permission)
def create_permission(permission: Permission):
    # Lógica para crear el permiso
    return permission

@router.get("/permissions", response_model=List[Permission])
def list_permissions():
    # Lógica para listar todos los permisos
    return []

@router.get("/permissions/{permission_id}", response_model=Permission)
def get_permission(permission_id: str):
    # Lógica para obtener un permiso por su id
    raise HTTPException(status_code=404, detail="Permission not found")

@router.put("/permissions/{permission_id}", response_model=Permission)
def update_permission(permission_id: str, permission: Permission):
    # Lógica para actualizar el permiso
    return permission

@router.delete("/permissions/{permission_id}")
def delete_permission(permission_id: str):
    # Lógica para eliminar el permiso
    return {"message": "Permission deleted"}

# ----------------------------------
# CRUD para la entidad Subscription
# ----------------------------------
@router.post("/subscriptions", response_model=Subscription)
def create_subscription(subscription: Subscription):
    # Lógica para crear la suscripción
    return subscription

@router.get("/subscriptions", response_model=List[Subscription])
def list_subscriptions():
    # Lógica para listar todas las suscripciones
    return []

@router.get("/subscriptions/{subscription_id}", response_model=Subscription)
def get_subscription(subscription_id: str):
    # Lógica para obtener una suscripción por su id
    raise HTTPException(status_code=404, detail="Subscription not found")

@router.put("/subscriptions/{subscription_id}", response_model=Subscription)
def update_subscription(subscription_id: str, subscription: Subscription):
    # Lógica para actualizar la suscripción
    return subscription

@router.delete("/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: str):
    # Lógica para eliminar la suscripción
    return {"message": "Subscription deleted"}
