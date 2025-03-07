"""
Módulo de Modelos de Datos para Permisos.

Ubicación:
    - Este módulo se encuentra en 'app/models/permission_model.py' y define el modelo de datos
      utilizado para representar un permiso asignado a un rol sobre un endpoint.

Responsabilidades:
    - Validar y estructurar la información relacionada con los permisos asignados a los roles,
      garantizando que cada permiso cumpla con las restricciones y formatos esperados.
    - Facilitar la interacción con la base de datos MongoDB mediante el mapeo de campos, como la conversión
      del campo '_id' de MongoDB al campo 'id' del modelo.
    - Representar atributos esenciales del permiso, incluyendo operaciones CRUD (create, read, update, delete)
      y metadatos de auditoría (fechas de creación, actualización y eliminación lógica).

Estructura:
    - Se define la clase Permission, que extiende BaseModel de Pydantic.
    - Se especifican atributos como:
         • _id: Identificador único generado por MongoDB.
         • role_id: Referencia al rol asociado (colección Role).
         • endpoint_id: Referencia al endpoint al que se aplican los permisos (colección Endpoint).
         • create, read, update, delete: Indicadores booleanos que determinan las operaciones permitidas.
         • created_at, updated_at, deleted_at: Fechas de creación, última actualización y eliminación lógica.
         • is_deleted: Indicador de eliminación lógica del registro.
    - La configuración interna de la clase permite la serialización personalizada del PyObjectId y el uso de alias para los campos.

Notas:
    - Se utiliza la zona horaria definida en 'app/config.py' para asignar los valores por defecto de los campos de fecha,
      garantizando la consistencia en la auditoría temporal.
    - La integración con PyObjectId asegura que el identificador único se maneje correctamente en los procesos de validación y serialización.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Permission(BaseModel):
    """
    Modelo de datos para representar un permiso asignado a un rol sobre un endpoint.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - role_id: Referencia al rol asociado con el permiso (colección Role).
      - endpoint_id: Referencia al endpoint al que se aplican los permisos (colección Endpoint).
      - create: Permiso para crear (POST) nuevos recursos en el endpoint.
      - read: Permiso para leer (GET) recursos del endpoint.
      - update: Permiso para modificar (PUT/PATCH) recursos existentes en el endpoint.
      - delete: Permiso para eliminar (DELETE) recursos en el endpoint.
      - created_at: Fecha y hora en que se creó el registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado el registro (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica del registro.
    """
    id: Optional[PyObjectId] = Field(
        default=None, alias="_id",
        description="Identificador único generado por MongoDB."
    )
    role_id: PyObjectId = Field(
        ..., 
        description="Referencia al rol asociado con el permiso (colección Role)."
    )
    endpoint_id: PyObjectId = Field(
        ..., 
        description="Referencia al endpoint al que se aplican los permisos (colección Endpoint)."
    )
    create: bool = Field(
        ..., 
        description="Permiso para crear (POST) nuevos recursos en el endpoint."
    )
    read: bool = Field(
        ..., 
        description="Permiso para leer (GET) recursos del endpoint."
    )
    update: bool = Field(
        ..., 
        description="Permiso para modificar (PUT/PATCH) recursos existentes en el endpoint."
    )
    delete: bool = Field(
        ..., 
        description="Permiso para eliminar (DELETE) recursos en el endpoint."
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora en que se creó el registro."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora de la última actualización del registro."
    )
    deleted_at: Optional[datetime] = Field(
        default=None, 
        description="Fecha y hora en que se marcó como eliminado el registro (eliminación lógica)."
    )
    is_deleted: bool = Field(
        default=False, 
        description="Indicador de eliminación lógica del registro."
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
