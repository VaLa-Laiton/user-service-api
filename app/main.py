import uvicorn
from fastapi import FastAPI
from app.db import mongodb 

app = FastAPI()

@app.get("/")
def welcome():
    return {"Mensaje": "Hola, que tal? Bienvenido a user-service-api"}


@app.get("/ping")
async def ping():
    return await mongodb.check_connection()


@app.post("/auth/register")
def auth_register():
    return {"Mensaje": "Esta es el end-point para registrar el usuario"}


@app.post("/auth/login")
def auth_login():
    return {"Mensaje": "Esta es el end-point para que un usuario inicie sesión"}


@app.get("/users/me")
def users_me():
    return {"Mensaje": "Esta es el end-point para obtener la data del usuario autenticado"}


@app.get("/users")
def users_all():
    return {"Mensaje": "Esta es el end-point para listar todos los usuarios existentes (Requiere permisos)"}


@app.put("/users/{id}")
def users_by_id():
    return {"Mensaje": "Esta es el end-point para modificar/editar los datos de un usuario"}