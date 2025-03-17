from fastapi import APIRouter, Depends, HTTPException 
from typing import List
from sqlmodel import select, Session
from database.session import get_session
from models.pregunta import Pregunta
from schemas.pregunta import PreguntaCreate, PreguntaRead
from crud.pregunta import *

router = APIRouter(prefix="/preguntas", tags=["Preguntas"])

@router.post("/", response_model=PreguntaRead)
def crear_pregunta(pregunta: PreguntaCreate, session: Session = Depends(get_session)):
    return crear_pregunta_service(pregunta, session)

@router.get("/", response_model=List[PreguntaRead])
def leer_preguntas(session: Session = Depends(get_session)):
    return leer_preguntas_service(session)

@router.get("/{pregunta_id}", response_model=PreguntaRead)
def leer_pregunta(pregunta_id: int, session: Session = Depends(get_session)):
    return leer_pregunta_service(pregunta_id, session)

@router.put("/{pregunta_id}", response_model=PreguntaRead)
def actualizar_pregunta(pregunta_id: int, pregunta: PreguntaCreate, session: Session = Depends(get_session)):
    return actualizar_pregunta_service(pregunta_id, pregunta, session)

@router.delete("/{pregunta_id}", response_model=PreguntaRead)
def eliminar_pregunta(pregunta_id: int, session: Session = Depends(get_session)):
    return eliminar_pregunta_service(pregunta_id, session)
