from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.usersrols, config.db, schemas.usersrols, models.usersrols
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador
key=Fernet.generate_key()
f = Fernet(key)

userrol = APIRouter()

models.usersrols.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@userrol.get("/usersrols/", response_model=List[schemas.usersrols.UserRol], tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def read_usersrols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usersrols= crud.usersrols.get_usersrols(db=db, skip=skip, limit=limit)
    return db_usersrols

@userrol.post("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def read_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol= crud.usersrols.get_userrol(db=db, id_user=id_user,id_rol=id_rol)

    if db_userrol is None:
        raise HTTPException(status_code=404, detail="UserRol no existe")
    return db_userrol


@userrol.post("/userrols/", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def create_user(userrol: schemas.usersrols.UserRolCreate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.get_userrol(db=db, id_user=userrol.Usuario_ID, id_rol=userrol.Rol_ID)
    print (db_userrol)
    if db_userrol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.usersrols.create_userrol(db=db, userrol=userrol)

@userrol.put("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def update_user(id_user: int, id_rol: int, userrol: schemas.usersrols.UserRolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.update_userrol(db=db, id_user=id_user, id_rol=id_rol, userrol=userrol)
    print (db_userrol.Estatus)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_userrol

@userrol.delete("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"], dependencies=[Depends(Portador())])
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.delete_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_userrol
