from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Permission(BaseModel):
    """
    Modelo de datos para representar un permiso asignado a un rol sobre un endpoint.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - role_id: Referencia al rol asociado con este permiso (colección Role).
      - endpoint_id: Referencia al endpoint al que se aplican los permisos (colección Endpoint).
      - create: Indica si se permite la operación de creación (POST) en el endpoint.
      - read: Indica si se permite la operación de lectura (GET) en el endpoint.
      - update: Indica si se permite la operación de actualización (PUT/PATCH) en el endpoint.
      - delete: Indica si se permite la operación de eliminación (DELETE) en el endpoint.
      - created_at: Fecha y hora de creación del registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado el registro (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica.
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
        json_encoders = {PyObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True
        from_attributes = True
