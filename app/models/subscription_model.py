from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Subscription(BaseModel):
    """
    Modelo de datos para representar una suscripción de una compañía en el sistema.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - company_id: Referencia al identificador único de la compañía asociada a la suscripción.
      - plan: Tipo de plan contratado (ej. "free", "basic", "premium", "individual").
      - max_users: Número máximo de usuarios permitidos bajo esta suscripción.
      - status: Estado actual de la suscripción ("active", "pending", "suspended" o "cancelled").
      - paid: Indica si la suscripción ha sido pagada.
      - start_date: Fecha en que la suscripción se activa.
      - expiration_date: Fecha en que finaliza el período de vigencia de la suscripción.
      - created_at: Fecha y hora en que se creó el registro.
      - updated_at: Fecha y hora de la última actualización del registro.
      - deleted_at: Fecha y hora en que se marcó como eliminado el registro (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica del registro.
    """
    id: Optional[PyObjectId] = Field(
        default=None,
        alias="_id",
        description="Identificador único generado por MongoDB."
    )
    company_id: PyObjectId = Field(
        ...,
        description="Referencia al identificador único de la compañía asociada a la suscripción."
    )
    plan: str = Field(
        ...,
        description="Tipo de plan contratado (ej. 'free', 'basic', 'premium', 'individual')."
    )
    max_users: int = Field(
        ...,
        description="Número máximo de usuarios permitidos bajo esta suscripción."
    )
    status: str = Field(
        ...,
        description="Estado actual de la suscripción ('active', 'pending', 'suspended', 'cancelled')."
    )
    paid: bool = Field(
        ...,
        description="Indica si la suscripción ha sido pagada."
    )
    start_date: datetime = Field(
        ...,
        description="Fecha en que la suscripción se activa."
    )
    expiration_date: datetime = Field(
        ...,
        description="Fecha en que finaliza el período de vigencia de la suscripción."
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
