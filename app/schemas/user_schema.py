from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import Optional

class User(BaseModel):
    """
    Esquema para la creación de un usuario.

    Este modelo define la estructura y validaciones para los datos
    requeridos al registrar un nuevo usuario en el sistema.
    """
    username: str = Field(..., description="Nombre de usuario.")
    email: EmailStr = Field(..., description="Correo electrónico válido.")
    full_name: str = Field(..., description="Nombre completo del usuario.")
    password: str = Field(..., description="Contraseña en texto plano.")
    phone_number: Optional[int] = Field(None, description="Número de teléfono del usuario (opcional).")
    avatar_url: Optional[AnyUrl] = Field(None, description="URL de la foto de perfil del usuario (opcional).")

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "test_user",
                "email": "testuser@example.com",
                "full_name": "Test User",
                "password": "MiContraseñaSegura123!",
                "phone_number": 3213908337,
                "avatar_url": "https://example.com/avatar.png"
            },
            "validation_info": {
                "note": "Las siguientes propiedades tienen una validación independiente antes de ser enviadas al modelo:",
                "fields": ["username", "email", "full_name", "password", "phone_number", "avatar_url"]
            }
        }
    }
