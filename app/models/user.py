from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime
from app.models.userRoles import UserRole
import pytz

# Define la zona horaria deseada
time_zone = pytz.timezone('America/Bogota')

class Users(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  # MongoDB asigna _id automáticamente si no se proporciona
    username: str = Field(..., min_length=3, max_length=50)  # Nombre de usuario con mínimo 3 y máximo 50 caracteres
    email: EmailStr  # Validación automática de correo electrónico
    full_name: Optional[str] = None  # Nombre completo del usuario
    hashed_password: str  # Contraseña almacenada en formato hash
    state: Literal["active", "inactive", "banned"] # Estado del usuario
    user_role: UserRole # Enum de los roles de usuarios disponibles
    is_active: bool = True  # Indica si el usuario está activo
    avatar_url: Optional[str] = None # Url de la foto de perfil del usuario

    last_login: Optional[datetime] = None # Fecha del ultimo inicio de sesión
    created_at: datetime = Field(default_factory=lambda: datetime.now(time_zone))  # Fecha de creación
    updated_at: datetime = Field(default_factory=lambda: datetime.now(time_zone))  # Fecha de última modificación
    deleted_at: Optional[datetime] = None  # Fecha de eliminación (None si no ha sido eliminado)
    is_deleted: bool = False  # Indica si el usuario ha sido eliminado (eliminación lógica)

    @staticmethod
    def holis():
        return f"Este es un metodo estatico que retorna la fecha y hora actual: {datetime.now(time_zone)}"

    class Config:
        populate_by_name = True  # Permite mapear "_id" a "id"
        from_attributes = True  # Habilita la compatibilidad con MongoDB
