"""
Middleware para medir y añadir el tiempo de procesamiento a cada solicitud HTTP.

Este middleware calcula el tiempo que tarda en procesarse una solicitud y
agrega este valor en la cabecera "X-Process-Time" de la respuesta.
"""

import time
from fastapi import Request

async def add_process_time_header(request: Request, call_next):
    """
    Middleware que mide el tiempo de procesamiento de la solicitud.

    Args:
        request (Request): La solicitud entrante.
        call_next (Callable): Función que procesa la siguiente etapa del middleware.

    Returns:
        Response: La respuesta HTTP con una cabecera adicional que indica el tiempo de procesamiento.
    """
    # Registrar el tiempo inicial antes de procesar la solicitud.
    start_time = time.perf_counter()
    
    # Procesar la solicitud y obtener la respuesta.
    response = await call_next(request)
    
    # Calcular el tiempo de procesamiento.
    process_time = time.perf_counter() - start_time
    
    # Añadir el tiempo de procesamiento en la cabecera de la respuesta.
    response.headers["X-Process-Time"] = str(process_time)
    
    return response
