from pydantic import BaseModel, Field
from app.models.userRoles import UserRole
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
    user_role: UserRole = Field(UserRole.TECHNICAL, description="Rol del usuario en el sistema.")
    is_active: bool = Field(True, description="Indica si el usuario está activo.")

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
                "is_active": True
            },
            "validation_info": {
                "note": "Las siguientes propiedades tienen una validación independiente antes de ser enviadas al modelo:",
                "fields": ["username", "password", "full_name", "email", "phone_number", "avatar_url"]
            }
        }
    }
