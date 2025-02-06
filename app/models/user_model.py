from pydantic import BaseModel, EmailStr, Field, AnyUrl, StringConstraints, PositiveInt
from typing import Optional, Literal
from datetime import datetime
from typing import Annotated
from app.models.userRoles import UserRole
import pytz

# Define la zona horaria deseada
time_zone = pytz.timezone('America/Bogota')

# Nota para mi yo futuro: ⚠️ Este dato debe validarse de forma independiente al modelo para proporcionar una respuesta más clara y comprensible para el usuario. => ref: *|⚠️⚠️⚠️|*
# Nota para mi yo futuro. Siempre que añadar un campo AQUÍ, tambien debes añadirlo al USER_SCHEMA.py❗❗❗

class Users(BaseModel):
    """
    Modelo de datos para representar a un usuario en el sistema.

    Este modelo se utiliza para validar y estructurar los datos de los usuarios,
    incluyendo información personal, credenciales, estado y metadatos de auditoría.
    """
    id: Optional[str] = Field(None, alias="_id")  # MongoDB asigna _id automáticamente si no se proporciona
    username: str = Field(..., min_length=3, max_length=50)  # Nombre de usuario con mínimo 3 y máximo 50 caracteres *|⚠️⚠️⚠️|*
    email: EmailStr  # Validación automática de correo electrónico *|⚠️⚠️⚠️|*
    phone_number: Optional[PositiveInt] = 0  # Número de teléfono del usuario *|⚠️⚠️⚠️|*
    full_name: Annotated[str, StringConstraints(min_length=3, max_length=50, pattern=r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s]+$")]  # Nombre completo del usuario *|⚠️⚠️⚠️|*
    password: str  # Contraseña almacenada en formato hash *|⚠️⚠️⚠️|*
    avatar_url: AnyUrl = None  # URL de la foto de perfil del usuario *|⚠️⚠️⚠️|*
    state: Literal["active", "inactive", "banned"] = "active"  # Estado del usuario
    user_role: UserRole = UserRole.TECHNICAL  # Enum de los roles de usuarios disponibles
    is_active: bool = True  # Indica si el usuario está activo

    last_login: Optional[datetime] = None  # Fecha del último inicio de sesión
    created_at: datetime = Field(default_factory=lambda: datetime.now(time_zone))  # Fecha de creación
    updated_at: datetime = Field(default_factory=lambda: datetime.now(time_zone))  # Fecha de última modificación
    deleted_at: Optional[datetime] = None  # Fecha de eliminación (None si no ha sido eliminado)
    is_deleted: bool = False  # Indica si el usuario ha sido eliminado (eliminación lógica)

    class Config:
        """
        Configuración adicional para el modelo Users.
        """
        populate_by_name = True  # Permite mapear "_id" a "id"
        from_attributes = True  # Habilita la compatibilidad con MongoDB
