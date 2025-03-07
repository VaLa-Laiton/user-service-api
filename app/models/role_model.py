from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Role(BaseModel):
    """
    Modelo de datos para representar un rol dentro de la aplicación.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - company_id: Referencia a la compañía a la que pertenece el rol.
      - name: Nombre descriptivo del rol (ej. "Administrator", "Editor", "Viewer").
      - description: Texto explicativo sobre las responsabilidades y alcances del rol.
      - created_at: Fecha y hora en que se creó el registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado el registro (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica del registro.
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
        json_encoders = {PyObjectId: str}
        allow_population_by_field_name = True
        populate_by_name = True
        from_attributes = True
