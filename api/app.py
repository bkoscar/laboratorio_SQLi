import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configura la conexión a la base de datos (si es necesario)
DATABASE_URL = os.getenv("DATABASE_URL")

# Página de inicio de sesión
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Procesar el formulario de inicio de sesión
@app.post("/login/")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Aquí puedes verificar las credenciales del usuario si es necesario
    
    # Si las credenciales son correctas, redirigir al usuario a la página de productos
    if username == "admin" and password == "admin":
        return templates.TemplateResponse("productos.html", {"request": request})
    # Si las credenciales son incorrectas, puedes lanzar una excepción HTTP o mostrar un mensaje de error
    return templates.TemplateResponse("login.html", {"request": request, "error_message": "Credenciales incorrectas"})

# ...

# Ruta para redirigir al formulario de ordenar
@app.get("/ordenar/")
async def order(request: Request):
    return templates.TemplateResponse("ordenar.html", {"request": request})


# Procesar el formulario de ordenar
@app.post("/procesar_orden")
async def process_order(request: Request, nombre: str = Form(...), direccion: str = Form(...)):
    return {"nombre": nombre, "direccion": "direccion"}
   