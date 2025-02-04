# **User Service API 🚀**  

📌 **Microservicio de Gestión de Usuarios - Python, FastAPI, MongoDB, Docker**  

## **Descripción**  

Este repositorio contiene un **microservicio REST API** para la gestión de usuarios, incluyendo autenticación, autorización y manejo de roles. Construido con **FastAPI**, utiliza **MongoDB** como base de datos y está completamente **contenedorizado con Docker** para facilitar su despliegue.  

## **Características**  

✅ **FastAPI**: Framework rápido y moderno para APIs en Python.  
✅ **Autenticación con JWT**: Manejo seguro de tokens para acceso de usuarios.  
✅ **MongoDB**: Base de datos NoSQL escalable para almacenamiento de usuarios.  
✅ **RBAC (Role-Based Access Control)**: Permisos basados en roles para mayor seguridad.  
✅ **Docker y Docker Compose**: Fácil despliegue en entornos locales y en la nube.  
✅ **Validación con Pydantic**: Datos seguros y consistentes en cada solicitud.  
✅ **Pruebas Automáticas**: Unit tests con `pytest` y `mongomock`.  

## **Tecnologías Utilizadas**  

🔹 **Lenguaje**: Python 3.x  
🔹 **Framework**: FastAPI  
🔹 **Base de Datos**: MongoDB  
🔹 **Autenticación**: JWT con PyJWT  
🔹 **Validación**: Pydantic  
🔹 **Contenedorización**: Docker y Docker Compose  
🔹 **Testing**: pytest, mongomock  
🔹 **Logs**: Loguru  

## **Instalación y Uso 🚀**  

### **Requisitos Previos**  

🔹 Tener **Docker** y **Docker Compose** instalados.  
🔹 Clonar este repositorio:  

```bash
git clone https://github.com/tu-usuario/user-service-api.git
cd user-service-api
```

### **Ejecutar con Docker**  

```bash
docker-compose up --build
```

La API estará disponible en **`http://localhost:8000/docs`** con documentación interactiva Swagger.

### **Ejecutar en Local (sin Docker)**  

1️⃣ Instalar dependencias:  

```bash
pip install -r requirements.txt
```

2️⃣ Configurar variables de entorno (`.env`):  

```env
MONGO_URI=mongodb://localhost:27017/users_db
JWT_SECRET=supersecreto
```

3️⃣ Ejecutar la API:  

```bash
uvicorn app.main:app --reload
```

## **Endpoints Principales**  

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/auth/register` | Registro de usuario |
| `POST` | `/auth/login` | Inicio de sesión y generación de JWT |
| `GET`  | `/users/me` | Obtener datos del usuario autenticado |
| `GET`  | `/users` | Listar usuarios (requiere permisos) |
| `PUT`  | `/users/{id}` | Modificar datos de usuario (admin) |

⚡ **Más detalles disponibles en** `http://localhost:8000/docs`

## **Pruebas**  

Ejecutar pruebas unitarias con:

```bash
pytest
```

## **Licencia**  

Este proyecto está bajo la licencia **Business Source License (BUSL-1.1)**.  
🔒 **Uso comercial no permitido sin autorización.** Contacta al autor para licencias comerciales.

---

🔹 **Contribuciones**: Abiertas para mejoras, pero con restricciones comerciales.  
🔹 **Contacto**: [Tu correo o GitHub Profile]  

📌 **Si necesitas una API escalable y segura para autenticación de usuarios, este microservicio es para ti. 🚀**
