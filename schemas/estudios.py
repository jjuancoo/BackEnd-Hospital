from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class EstudiosBase(BaseModel):
    Tipo: str
    Nivel_Urgencia: str
    # Solicitud_ID: int
    # Consumibles_ID: Optional[int] = None
    Estatus: str
    Total_Costo: Decimal
    Dirigido_A: Optional[str] = None
    Observaciones: Optional[str] = None
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

class EstudiosCreate(EstudiosBase):
    pass

class EstudiosUpdate(EstudiosBase):
    pass

class Estudios(EstudiosBase):
    ID: int

    class Config:
        from_attributes = True