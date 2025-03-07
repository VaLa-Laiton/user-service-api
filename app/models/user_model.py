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
    - Definir campos esenciales del usuario, incluyendo credenciales, datos personales, relaciones (con Role y Company)
      y metadatos de auditoría (fechas de creación, actualización, eliminación, etc.).
    - Incluir validaciones adicionales:
         • El campo full_name se valida con una expresión regular que permite únicamente letras (incluyendo caracteres acentuados)
           y espacios.
         • El campo state se restringe a los valores "active", "inactive" o "banned".

Notas:
    - Este modelo debe mantenerse sincronizado con el esquema definido en USER_SCHEMA.py. Cada modificación en la
      estructura de este modelo debe reflejarse en el esquema correspondiente.
    - La zona horaria utilizada para los campos de fecha se importa desde 'app/config.py', garantizando la consistencia
      en el manejo temporal a nivel global en la aplicación.
"""

from pydantic import BaseModel, Field, EmailStr, AnyUrl, PositiveInt, constr
from typing import Optional, Literal, Annotated
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId  # Importamos PyObjectId desde app.config

class User(BaseModel):
    """
    Modelo de datos para representar a un usuario en el sistema.

    Incluye:
      - Identificador (_id) generado por MongoDB.
      - Relaciones: role_id y company_id (referencias a Role y Company).
      - Datos personales, credenciales, perfil y metadatos de auditoría.
      - Validaciones específicas, como:
            • El campo full_name solo acepta letras y espacios.
            • El campo state está restringido a "active", "inactive" o "banned".
    """
    id: Optional[PyObjectId] = Field(
        default=None, alias="_id", 
        description="Identificador único generado por MongoDB."
    )
    role_id: Optional[PyObjectId] = Field(
        default=None, 
        description="Referencia al rol asignado al usuario (colección Role)."
    )
    company_id: Optional[PyObjectId] = Field(
        default=None, 
        description="Referencia a la compañía asociada al usuario (colección Company)."
    )
    username: str = Field(
        ..., min_length=3, max_length=50, 
        description="Nombre de usuario único."
    )
    email: EmailStr = Field(
        ..., 
        description="Correo electrónico único y válido."
    )
    phone_number: Optional[PositiveInt] = Field(
        None, 
        description="Número de teléfono (valor numérico positivo)."
    )
    full_name: Annotated[
        str,
        constr(min_length=3, max_length=50, regex=r"^[a-zA-ZÀ-ÖØ-öø-ÿ\s]+$")
    ] = Field(
        ..., 
        description="Nombre completo, compuesto solo por letras y espacios."
    )
    password: str = Field(
        ..., 
        description="Contraseña almacenada en formato hash."
    )
    is_temp_password: bool = Field(
        default=False, 
        description="Indica si la contraseña actual es temporal."
    )
    avatar_url: Optional[AnyUrl] = Field(
        None, 
        description="URL de la foto de perfil del usuario."
    )
    state: Literal["active", "inactive", "banned"] = Field(
        default="active", 
        description="Estado de la cuenta del usuario."
    )
    last_login: Optional[datetime] = Field(
        None, 
        description="Fecha y hora del último inicio de sesión."
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora en que se creó el usuario."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora de la última actualización del registro."
    )
    deleted_at: Optional[datetime] = Field(
        None, 
        description="Fecha y hora en que se marcó como eliminado el usuario (eliminación lógica)."
    )
    is_deleted: bool = Field(
        default=False, 
        description="Indicador de eliminación lógica del usuario."
    )

class Config:
    # Define cómo se serializan los objetos de tipo PyObjectId en salidas JSON, convirtiéndolos a cadenas.
    json_encoders = {PyObjectId: str}
    
    # Permite que los campos del modelo sean poblados utilizando sus nombres definidos en el modelo,
    # además de sus alias, lo que facilita la asignación de valores durante la instanciación.
    allow_population_by_field_name = True
    
    # Habilita la población de datos en el modelo utilizando los nombres de los campos, asegurando que
    # se puedan asignar valores correctamente incluso cuando se usan alias.
    populate_by_name = True
    
    # Permite crear instancias del modelo a partir de objetos que tengan atributos coincidentes con los campos
    # definidos en el modelo, facilitando la conversión y la interoperabilidad de datos.
    from_attributes = True
