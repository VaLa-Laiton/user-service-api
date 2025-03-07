"""
Módulo de Modelos de Datos para Roles.

Ubicación:
    - Este módulo se encuentra en 'app/models/role_model.py' y define el modelo de datos
      utilizado para representar un rol dentro de la aplicación.

Responsabilidades:
    - Validar y estructurar los datos de los roles mediante Pydantic, asegurando que la información
      cumpla con las restricciones y formatos esperados.
    - Facilitar la interacción con la base de datos MongoDB mediante el mapeo de campos, como transformar
      el campo '_id' de MongoDB al campo 'id' del modelo.
    - Representar atributos esenciales del rol, incluyendo su identificación, la compañía asociada, descripción,
      y metadatos de auditoría (fechas de creación, actualización y eliminación lógica).

Estructura:
    - Se define la clase Role que extiende BaseModel de Pydantic.
    - Se especifican atributos como:
         • _id: Identificador único generado por MongoDB.
         • company_id: Referencia a la compañía a la que pertenece el rol.
         • name: Nombre descriptivo del rol.
         • description: Descripción detallada sobre las responsabilidades y alcances del rol.
         • created_at, updated_at, deleted_at: Fechas de creación, última actualización y eliminación lógica.
         • is_deleted: Indicador de eliminación lógica del registro.
    - La configuración interna de la clase permite la serialización personalizada de PyObjectId y
      el uso de alias para los campos.

Notas:
    - La integración con PyObjectId asegura la validación y conversión correcta del identificador único.
    - Se utiliza una función lambda para asignar los valores por defecto de los campos de fecha, utilizando
      la zona horaria definida en la configuración global.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Role(BaseModel):
    """
    Modelo de datos para representar un rol dentro de la aplicación.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - company_id: Referencia al identificador de la compañía a la que pertenece este rol.
      - name: Nombre descriptivo del rol (ej. "Administrator", "Editor", "Viewer").
      - description: Texto explicativo sobre las responsabilidades y alcances del rol.
      - created_at: Fecha y hora en que se creó el rol.
      - updated_at: Fecha y hora de la última actualización del rol.
      - deleted_at: Fecha y hora en que se marcó como eliminado el rol (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica del rol.
    """
    id: Optional[PyObjectId] = Field(
        default=None, alias="_id",
        description="Identificador único generado por MongoDB."
    )
    company_id: PyObjectId = Field(
        ...,
        description="Referencia al identificador de la compañía a la que pertenece este rol."
    )
    name: str = Field(
        ...,
        description="Nombre descriptivo del rol."
    )
    description: Optional[str] = Field(
        None,
        description="Descripción detallada sobre el rol."
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE),
        description="Fecha y hora en que se creó el rol."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE),
        description="Fecha y hora de la última actualización del rol."
    )
    deleted_at: Optional[datetime] = Field(
        None,
        description="Fecha y hora en que se marcó como eliminado el rol (eliminación lógica)."
    )
    is_deleted: bool = Field(
        default=False,
        description="Indicador de eliminación lógica del rol."
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
