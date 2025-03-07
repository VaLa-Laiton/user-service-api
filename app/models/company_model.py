from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Company(BaseModel):
    """
    Modelo de datos para representar una compañía en el sistema.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - name: Nombre de la compañía, que puede asignarse de forma automática o manual.
      - description: Breve descripción de la actividad o propósito de la compañía.
      - owner: Referencia al usuario que creó la compañía (propietario), representado por un ObjectId.
      - created_at: Fecha y hora en que se creó el registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado el registro (para eliminación lógica).
      - is_deleted: Indicador de eliminación lógica.
    """
    id: Optional[PyObjectId] = Field(
        default=None, alias="_id",
        description="Identificador único generado por MongoDB."
    )
    name: str = Field(
        ..., 
        description="Nombre de la compañía."
    )
    description: Optional[str] = Field(
        None, 
        description="Descripción breve de la compañía."
    )
    owner: PyObjectId = Field(
        ..., 
        description="Referencia al usuario que es el propietario o creador de la compañía."
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora en que se creó la compañía."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE), 
        description="Fecha y hora de la última actualización del registro."
    )
    deleted_at: Optional[datetime] = Field(
        None, 
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
