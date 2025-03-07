"""
Módulo de Modelo para la Gestión de Compañías.

Ubicación:
    - Este módulo se encuentra en 'app/models/company_model.py' y define el modelo de datos
      utilizado para representar una compañía en el sistema.

Responsabilidades:
    - Definir la estructura de datos para una compañía utilizando Pydantic.
    - Validar y documentar los atributos requeridos para la gestión de compañías.
    - Integrar configuraciones globales, como la zona horaria (TIME_ZONE) y la validación de ObjectId (PyObjectId).

Estructura:
    - Se define la clase Company que extiende BaseModel de Pydantic.
    - Se especifican atributos como:
         • _id: Identificador único generado por MongoDB.
         • name: Nombre de la compañía.
         • description: Breve descripción de la compañía.
         • owner: Referencia al usuario que es propietario o creador de la compañía.
         • created_at, updated_at, deleted_at: Fechas de creación, última actualización y eliminación lógica.
         • is_deleted: Indicador de eliminación lógica del registro.
    - La configuración interna de la clase permite la serialización personalizada y el uso de alias para los campos.

Notas:
    - La integración con PyObjectId asegura la validación y conversión correcta del identificador único.
    - Se utilizan funciones lambda para asignar valores por defecto a los campos de fecha, aprovechando la zona horaria configurada.
"""

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
