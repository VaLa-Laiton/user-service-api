"""
Módulo de Modelos de Datos para Endpoints de la API.

Ubicación:
    - Este módulo se encuentra en 'app/models/endpoint_model.py' y define el modelo de datos utilizado
      para representar un endpoint de la API.

Responsabilidades:
    - Validar y estructurar la información relacionada con los endpoints de la API mediante Pydantic.
    - Facilitar la interacción con la base de datos MongoDB mediante el mapeo de campos, incluyendo la conversión
      del campo '_id' al campo 'id' del modelo.
    - Permitir la auditoría de endpoints a través de metadatos como fechas de creación, actualización y eliminación lógica.

Estructura:
    - Se define la clase Endpoint, que extiende BaseModel de Pydantic.
    - Se especifican atributos esenciales, tales como:
         • _id: Identificador único generado por MongoDB.
         • path: Ruta o URL exacta que identifica el endpoint.
         • name: Nombre corto y descriptivo del endpoint.
         • description: Descripción detallada del propósito y funcionamiento del endpoint.
         • created_at, updated_at, deleted_at: Fechas de creación, última actualización y eliminación lógica.
         • is_deleted: Indicador de eliminación lógica del registro.
    - La configuración interna de la clase permite la serialización personalizada del PyObjectId y el uso de alias para los campos.

Notas:
    - Se utiliza la zona horaria definida en 'app/config.py' para asignar los valores por defecto de los campos de fecha,
      asegurando la consistencia en la auditoría temporal.
    - La integración con PyObjectId garantiza que el identificador único se maneje correctamente en los procesos de validación y serialización.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.config import TIME_ZONE, PyObjectId

class Endpoint(BaseModel):
    """
    Modelo de datos para representar un endpoint de la API.

    Atributos:
      - _id: Identificador único generado por MongoDB.
      - path: Ruta o URL exacta del endpoint.
      - name: Nombre corto y descriptivo del endpoint.
      - description: Descripción detallada del propósito y funcionamiento del endpoint.
      - created_at: Fecha y hora en que se creó el endpoint.
      - updated_at: Fecha y hora de la última actualización del endpoint.
      - deleted_at: Fecha y hora en que se marcó como eliminado el endpoint (eliminación lógica).
      - is_deleted: Indicador de eliminación lógica del endpoint.
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
