from sqlalchemy.orm import Session
import models.estudios
import schemas.estudios

def get_estudio(db: Session, id: int):
    return db.query(models.estudios.Estudios).filter(models.estudios.Estudios.ID == id).first()

def get_estudios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.estudios.Estudios).offset(skip).limit(limit).all()

def create_estudio(db: Session, estudio: schemas.estudios.EstudiosCreate):
    db_estudio = models.estudios.Estudios(
        Tipo=estudio.Tipo,
        Nivel_Urgencia=estudio.Nivel_Urgencia,
        # Solicitud_ID=estudio.Solicitud_ID,
        # Consumibles_ID=estudio.Consumibles_ID,
        Estatus=estudio.Estatus,
        Total_Costo=estudio.Total_Costo,
        Dirigido_A=estudio.Dirigido_A,
        Observaciones=estudio.Observaciones,
        Fecha_Registro=estudio.Fecha_Registro,
        Fecha_Actualizacion=estudio.Fecha_Actualizacion,
    )
    db.add(db_estudio)
    db.commit()
    db.refresh(db_estudio)
    return db_estudio

def update_estudio(db: Session, id: int, estudio: schemas.estudios.EstudiosUpdate):
    db_estudio = db.query(models.estudios.Estudios).filter(models.estudios.Estudios.ID == id).first()
    if db_estudio:
        for var, value in vars(estudio).items():
            setattr(db_estudio, var, value) if value else None
        db.commit()
        db.refresh(db_estudio)
    return db_estudio

def delete_estudio(db: Session, id: int):
    db_estudio = db.query(models.estudios.Estudios).filter(models.estudios.Estudios.ID == id).first()
    if db_estudio:
        db.delete(db_estudio)
        db.commit()
    return db_estudio
