from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from database.models import Respuesta
from app.database.session import get_session

router = APIRouter(prefix="/respuestas", tags=["Respuestas"])

@router.post("/", response_model=Respuesta)
def crear_respuesta(respuesta: Respuesta, session: Session = Depends(get_session)):
    session.add(respuesta)
    session.commit()
    session.refresh(respuesta)
    return respuesta

@router.get("/", response_model=List[Respuesta])
def leer_respuestas(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    respuestas = session.exec(select(Respuesta).offset(skip).limit(limit)).all()
    return respuestas

@router.get("/{respuesta_id}", response_model=Respuesta)
def leer_respuesta(respuesta_id: int, session: Session = Depends(get_session)):
    respuesta = session.get(Respuesta, respuesta_id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    return respuesta

@router.put("/{respuesta_id}", response_model=Respuesta)
def actualizar_respuesta(respuesta_id: int, respuesta: Respuesta, session: Session = Depends(get_session)):
    db_respuesta = session.get(Respuesta, respuesta_id)
    if not db_respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    respuesta_data = respuesta.dict(exclude_unset=True)
    for key, value in respuesta_data.items():
        setattr(db_respuesta, key, value)
    session.add(db_respuesta)
    session.commit()
    session.refresh(db_respuesta)
    return db_respuesta

@router.delete("/{respuesta_id}", response_model=Respuesta)
def eliminar_respuesta(respuesta_id: int, session: Session = Depends(get_session)):
    respuesta = session.get(Respuesta, respuesta_id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    session.delete(respuesta)
    session.commit()
    return respuesta
