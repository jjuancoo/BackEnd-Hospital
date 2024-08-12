from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date

class RolBase(BaseModel):
    Nombre: str
    Descripcion: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    ID: int
    class Config:
        orm_mode = True


