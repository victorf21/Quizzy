from sqlmodel import Session, select
from fastapi import HTTPException
from models.pregunta import Pregunta
from schemas.pregunta import PreguntaCreate

def crear_pregunta_service(pregunta: PreguntaCreate, session: Session):
    nueva_pregunta = Pregunta(**pregunta.dict())
    session.add(nueva_pregunta)
    session.commit()
    session.refresh(nueva_pregunta)
    return nueva_pregunta

def leer_preguntas_service(session: Session):
    return session.exec(select(Pregunta)).all()

def leer_pregunta_service(pregunta_id: int, session: Session):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return pregunta

def actualizar_pregunta_service(pregunta_id: int, pregunta: PreguntaCreate, session: Session):
    db_pregunta = session.get(Pregunta, pregunta_id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    for key, value in pregunta.dict(exclude_unset=True).items():
        setattr(db_pregunta, key, value)
    session.commit()
    session.refresh(db_pregunta)
    return db_pregunta

def eliminar_pregunta_service(pregunta_id: int, session: Session):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    session.delete(pregunta)
    session.commit()
    return pregunta
