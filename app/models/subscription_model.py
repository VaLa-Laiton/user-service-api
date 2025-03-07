"""
Módulo de Modelos de Datos para Suscripciones.

Ubicación:
    - Este módulo se encuentra en 'app/models/subscription_model.py' y define el modelo de datos
      utilizado para representar una suscripción de una compañía en el sistema.

Responsabilidades:
    - Validar y estructurar la información de las suscripciones mediante Pydantic, asegurando que cada
      registro cumpla con las restricciones y formatos esperados.
    - Facilitar la interacción con la base de datos MongoDB mediante el mapeo de campos, transformando el
      campo '_id' de MongoDB al campo 'id' del modelo.
    - Representar atributos esenciales de una suscripción, incluyendo detalles del plan contratado, límites de usuarios,
      estado de la suscripción, y metadatos de auditoría (fechas de creación, actualización y eliminación lógica).

Estructura:
    - Se define la clase Subscription que extiende BaseModel de Pydantic.
    - Se especifican atributos como:
         • _id: Identificador único generado por MongoDB.
         • company_id: Referencia al identificador único de la compañía asociada.
         • plan: Tipo de plan contratado (ej. 'free', 'basic', 'premium', 'individual').
         • max_users: Número máximo de usuarios permitidos bajo la suscripción.
         • status: Estado actual de la suscripción ('active', 'pending', 'suspended', 'cancelled').
         • paid: Indicador booleano que señala si la suscripción ha sido pagada.
         • start_date: Fecha en que la suscripción se activa.
         • expiration_date: Fecha en que finaliza el período de vigencia de la suscripción.
         • created_at, updated_at, deleted_at: Fechas de creación, última actualización y eliminación lógica.
         • is_deleted: Indicador de eliminación lógica del registro.
    - La configuración interna de la clase permite la serialización personalizada del PyObjectId y
      el uso de alias para los campos.

Notas:
    - Se utiliza la zona horaria definida en 'app/config.py' para asignar los valores por defecto de los campos de fecha,
      garantizando la consistencia en la auditoría temporal.
    - La integración con PyObjectId asegura el manejo correcto del identificador único en los procesos de validación y serialización.
"""

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
      - status: Estado actual de la suscripción ("active", "pending", "suspended", "cancelled").
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
