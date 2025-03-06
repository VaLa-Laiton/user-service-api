from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Endpoint(BaseModel):
    """
    Modelo de datos para representar un endpoint de la API.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - path: Ruta o URL exacta que identifica el endpoint.
      - name: Nombre corto y descriptivo del endpoint.
      - description: Explicación detallada del propósito y funcionamiento del endpoint.
      - created_at: Fecha y hora en que se creó el registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica.
    """
    id: Optional[PyObjectId] = Field(
        default=None,
        alias="_id",
        description="Identificador único generado por MongoDB."
    )
    path: str = Field(
        ...,
        description="Ruta o URL exacta del endpoint."
    )
    name: str = Field(
        ...,
        description="Nombre corto y descriptivo del endpoint."
    )
    description: str = Field(
        ...,
        description="Descripción detallada del propósito y funcionamiento del endpoint."
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE),
        description="Fecha y hora en que se creó el endpoint."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(TIME_ZONE),
        description="Fecha y hora de la última actualización del endpoint."
    )
    deleted_at: Optional[datetime] = Field(
        None,
        description="Fecha y hora en que se marcó como eliminado el endpoint (eliminación lógica)."
    )
    is_deleted: bool = Field(
        default=False,
        description="Indicador de eliminación lógica del endpoint."
    )

    class Config:
        json_encoders = {PyObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True
        from_attributes = True
