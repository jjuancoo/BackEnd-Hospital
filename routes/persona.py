from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

persona = APIRouter()
personas = []

class ModelPersonas(BaseModel):
    id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str]
    edad: int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    creacion_at: datetime = datetime.now()
    estatus: bool = False

@persona.get("/")
def bienvenida():
    return "Bienvenido al API"

@persona.get("/personas")
def get_personas():
    return personas

@persona.post("/personas")
def save_personas(datos_personas: ModelPersonas):
    personas.append(datos_personas)
    return "Datos Guardados Correctamente"

@persona.get("/personas/{persona_id}")
def get_persona(persona_id: int):
    for persona in personas:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")



@persona.put("/personas/{persona_id}")
def update_persona(persona_id: int, datos_personas: ModelPersonas):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = datos_personas
            return "Datos Actualizados Correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@persona.delete("/personas/{persona_id}")
def delete_persona(persona_id: int):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas.pop(index)
            return "Datos Eliminados Correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")