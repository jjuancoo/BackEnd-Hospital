from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.estudios, config.db, schemas.estudios, models.estudios
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

estudios = APIRouter()

models.estudios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@estudios.get("/estudios/", response_model=List[schemas.estudios.Estudios], tags=["Estudios"], dependencies=[Depends(Portador())])
def read_estudios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_estudios = crud.estudios.get_estudios(db=db, skip=skip, limit=limit)
    return db_estudios

@estudios.get("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
def read_estudio(id: int, db: Session = Depends(get_db)):
    db_estudio = crud.estudios.get_estudio(db=db, id=id)
    if db_estudio is None:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return db_estudio

@estudios.post("/estudio/", response_model=schemas.estudios.Estudios, tags=["Estudios"])
def create_estudio(estudio: schemas.estudios.EstudiosCreate, db: Session = Depends(get_db)):
    # Asumiendo que no hay un método para verificar duplicados de 'Estudio'
    return crud.estudios.create_estudio(db=db, estudio=estudio)

@estudios.put("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
def update_estudio(id: int, estudio: schemas.estudios.EstudiosUpdate, db: Session = Depends(get_db)):
    db_estudio = crud.estudios.update_estudio(db=db, id=id, estudio=estudio)
    if db_estudio is None:
        raise HTTPException(status_code=404, detail="Estudio no existe, no actualizado")
    return db_estudio

@estudios.delete("/estudio/{id}", response_model=schemas.estudios.Estudios, tags=["Estudios"], dependencies=[Depends(Portador())])
def delete_estudio(id: int, db: Session = Depends(get_db)):
    db_estudio = crud.estudios.delete_estudio(db=db, id=id)
    if db_estudio is None:
        raise HTTPException(status_code=404, detail="Estudio no existe, no se pudo eliminar")
    return db_estudio
