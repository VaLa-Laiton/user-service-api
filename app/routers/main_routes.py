from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.db import mongodb 

router = APIRouter()

@router.get("/")
def welcome():
    """
    Endpoint de bienvenida.

    Returns:
        dict: Mensaje de bienvenida en formato JSON.
    """
    return {"Mensaje": "Hola, que tal? Bienvenido a user-service-api"}

@router.get("/ping")
async def ping():
    """
    Endpoint para verificar la conexión a la base de datos.

    Returns:
        JSONResponse: Resultado de la verificación de conexión a MongoDB.
    """
    return await mongodb.check_connection()
