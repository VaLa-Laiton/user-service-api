from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    """
    Esquema para la creación de un usuario.

    Este modelo define la estructura y validaciones para los datos
    requeridos al registrar un nuevo usuario en el sistema.
    """
    id: Optional[str] = Field(None, description="ID del usuario en la base de datos.")
    username: str = Field(..., description="Nombre de usuario.")
    email: str = Field(..., description="Correo electrónico válido.")
    phone_number: int = Field(..., description="Número de teléfono del usuario.")
    full_name: str = Field(..., description="Nombre completo del usuario.")
    password: str = Field(..., description="Contraseña en texto plano.")
    avatar_url: str = Field(..., description="URL de la foto de perfil del usuario.")
    state: str = Field("active", description="Estado del usuario: active, inactive o banned.")
    user_role: str = Field(..., description="Rol del usuario en el sistema.")
    is_active: bool = Field(True, description="Indica si el usuario está activo.")
    last_login: Optional[str] = Field(None, description="Fecha y hora del último inicio de sesión en formato ISO.")
    created_at: Optional[str] = Field(None, description="Fecha y hora de creación del usuario en formato ISO.")
    updated_at: Optional[str] = Field(None, description="Fecha y hora de la última actualización en formato ISO.")
    deleted_at: Optional[str] = Field(None, description="Fecha de eliminación (si aplica) en formato ISO.")
    is_deleted: bool = Field(False, description="Indica si el usuario ha sido eliminado.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "67a4d6e241b7de3dc3cfaec7",
                "username": "test_user",
                "email": "testuser@example.com",
                "phone_number": 3213908337,
                "full_name": "Test User",
                "password": "MiContraseñaSegura123!",
                "avatar_url": "https://example.com/avatar.png",
                "state": "active",
                "user_role": "technical",
                "is_active": True,
                "last_login": None,
                "created_at": "2025-02-06T10:07:51.261507-05:00",
                "updated_at": "2025-02-06T10:07:51.261551-05:00",
                "deleted_at": None,
                "is_deleted": False
            },
            "validation_info": {
                "note": "Las siguientes propiedades tienen una validación independiente antes de ser enviadas al modelo:",
                "fields": ["username", "password", "full_name", "email", "phone_number", "avatar_url"]
            }
        }
    }
