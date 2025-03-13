from fastapi import APIRouter, Depends, HTTPException 
from typing import List
from sqlmodel import select, Session
from database.session import get_session
from models.pregunta import Pregunta
from schemas.pregunta import PreguntaCreate, PreguntaRead

router = APIRouter(prefix="/preguntas", tags=["Preguntas"])

@router.post("/", response_model=PreguntaRead)
def crear_pregunta(pregunta: PreguntaCreate, session: Session = Depends(get_session)):
    nueva_pregunta = Pregunta(**pregunta.dict())
    session.add(nueva_pregunta)
    session.commit()
    session.refresh(nueva_pregunta)
    return nueva_pregunta

@router.get("/", response_model=List[PreguntaRead])
def leer_preguntas(session: Session = Depends(get_session)):
    preguntas = session.exec(select(Pregunta)).all()
    return preguntas

@router.get("/{pregunta_id}", response_model=PreguntaRead)
def leer_pregunta(pregunta_id: int, session: Session = Depends(get_session)):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return pregunta

@router.put("/{pregunta_id}", response_model=PreguntaRead)
def actualizar_pregunta(pregunta_id: int, pregunta: PreguntaCreate, session: Session = Depends(get_session)):
    db_pregunta = session.get(Pregunta, pregunta_id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    for key, value in pregunta.dict(exclude_unset=True).items():
        setattr(db_pregunta, key, value)
    session.commit()
    session.refresh(db_pregunta)
    return db_pregunta

@router.delete("/{pregunta_id}", response_model=PreguntaRead)
def eliminar_pregunta(pregunta_id: int, session: Session = Depends(get_session)):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    session.delete(pregunta)
    session.commit()
    return pregunta
