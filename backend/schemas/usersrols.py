from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserRolBase(BaseModel):
    Usuario_ID: int
    Rol_ID: int
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserRolCreate(UserRolBase):
    pass

class UserRolUpdate(UserRolBase):
    pass

class UserRol(UserRolBase):
    Usuario_ID: int
    Rol_ID: int
    class Config:
        orm_mode = True


