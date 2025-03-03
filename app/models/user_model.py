"""
Módulo de Modelos de Datos para Usuarios.

Ubicación:
    - Este módulo se encuentra en 'app/models/user_model.py' y define la estructura y validación de la información
      relacionada con los usuarios de la aplicación.

Responsabilidades:
    - Validar y estructurar los datos de los usuarios mediante Pydantic, garantizando que la información cumpla
      con las restricciones y formatos esperados.
    - Facilitar la interacción con la base de datos MongoDB mediante el mapeo de campos, por ejemplo, mapeando '_id'
      de MongoDB al campo 'id' del modelo.
    - Definir campos esenciales del usuario, tales como credenciales, datos personales, estado de la cuenta, roles y
      metadatos de auditoría (fechas de creación, actualización, eliminación, etc.).

Notas:
    - Este modelo debe mantenerse sincronizado con el esquema definido en USER_SCHEMA.py. Cada modificación en la
      estructura de este modelo debe reflejarse en el esquema correspondiente.
    - La zona horaria utilizada para los campos de fecha se importa desde 'app/config.py', garantizando así la
      consistencia en el manejo temporal a nivel global en la aplicación.
"""

from pydantic import BaseModel, EmailStr, Field, AnyUrl, StringConstraints, PositiveInt
from typing import Optional, Literal, Annotated
from datetime import datetime
from app.config import TIME_ZONE  # Utilizar la zona horaria configurada globalmente

# Nota para mi yo futuro: ⚠️ Este dato debe validarse de forma independiente al modelo para proporcionar una respuesta más clara y comprensible para el usuario.
# Nota para mi yo futuro: Siempre que añadas un campo AQUÍ, también debes añadirlo al USER_SCHEMA.py❗❗❗

class Users(BaseModel):
    """
    Modelo de datos para representar a un usuario en el sistema.

    Este modelo se utiliza para validar y estructurar la información de los usuarios, abarcando datos personales,
    credenciales, estado de la cuenta y metadatos de auditoría. Utiliza Pydantic para asegurar que la información
    cumpla con las restricciones definidas y se integre correctamente con la base de datos MongoDB.
    """
    id: Optional[str] = Field(None, alias="_id")  # MongoDB asigna '_id' automáticamente si no se proporciona
    username: str = Field(..., min_length=3, max_length=50)  # Nombre de usuario con mínimo 3 y máximo 50 caracteres
    email: EmailStr  # Validación automática del formato de correo electrónico
    phone_number: Optional[PositiveInt] = 0  # Número de teléfono del usuario (valor numérico positivo)
    full_name: Annotated[
        str,
        StringConstraints(min_length=3, max_length=50, pattern=r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s]+$")
    ]  # Nombre completo del usuario, restringido a letras y espacios
    password: str  # Contraseña del usuario, almacenada en formato hash
    avatar_url: AnyUrl = None  # URL de la foto de perfil del usuario
    state: Literal["active", "inactive", "banned"] = "active"  # Estado de la cuenta del usuario
    user_role: str # Rol del usuario ⚠️⚠️⚠️ Por el momento se dejara como un str, hazta implementar toda la logica de las demas entidades.
    is_active: bool = True  # Indica si el usuario está activo

    last_login: Optional[datetime] = None  # Fecha del último inicio de sesión
    created_at: datetime = Field(default_factory=lambda: datetime.now(TIME_ZONE))  # Fecha de creación, utilizando la zona horaria global
    updated_at: datetime = Field(default_factory=lambda: datetime.now(TIME_ZONE))  # Fecha de última modificación, utilizando la zona horaria global
    deleted_at: Optional[datetime] = None  # Fecha de eliminación (None si el usuario no ha sido eliminado)
    is_deleted: bool = False  # Indicador de eliminación lógica del usuario

    class Config:
        """
        Configuración adicional para el modelo Users.

        - populate_by_name: Permite mapear el campo '_id' de MongoDB al campo 'id' en el modelo.
        - from_attributes: Habilita la compatibilidad con objetos directamente obtenidos de MongoDB.
        """
        populate_by_name = True
        from_attributes = True
