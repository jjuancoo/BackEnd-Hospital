from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime


usuario= APIRouter()
usuarios = []

class model_usuarios(BaseModel):
    id: str
    usuario: str
    contrasena: str
    id_persona: str
    estatus: bool = True
    created_at: datetime = datetime.now()

@usuario.get('/usuarios')
def get_usuarios():
    return usuarios

@usuario.post('/usuarios')
def save_usuario(datos_usuario: model_usuarios):
    usuarios.append(datos_usuario)
    return "Usuario guardado correctamente"

@usuario.get('/usuarios/{usuario_id}')
def get_usuario(usuario_id: str):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@usuario.put('/usuarios/{usuario_id}')

def update_usuario(usuario_id: str, datos_actualizados: model_usuarios):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[index].usuario = datos_actualizados.usuario
            usuarios[index].contrasena = datos_actualizados.contrasena
            usuarios[index].id_persona = datos_actualizados.id_persona
            usuarios[index].estatus = datos_actualizados.estatus
            usuarios[index].created_at = datos_actualizados.created_at
            return "Usuario actualizado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



@usuario.delete('/usuarios/{usuario_id}')
def delete_usuario(usuario_id: str):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            del usuarios[index]
            return "Usuario eliminado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")