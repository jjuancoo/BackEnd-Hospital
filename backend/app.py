from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol

app=FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print ("Hola bienvenido a mi backend")
