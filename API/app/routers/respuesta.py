from fastapi import APIRouter, Depends
from sqlmodel import Session
from schemas.respuesta import RespuestaRead, RespuestaCreate, RespuestaUpdate
from database.session import get_session
from crud.respuesta import *

router = APIRouter(prefix="/respuesta", tags=["Respuesta"])

@router.post("/respuesta/", response_model=RespuestaRead)
def crear_respuesta(respuesta: RespuestaCreate, session: Session = Depends(get_session)):
    return create_respuesta(session, respuesta)

@router.get("/respuesta/{id}", response_model=RespuestaRead)
def obtener_respuesta(id: int, session: Session = Depends(get_session)):
    return get_respuesta(session, id)

@router.get("/pregunta/{id_pregunta}/respuestas", response_model=list[RespuestaRead])
def obtener_respuestas_por_pregunta(id_pregunta: int, session: Session = Depends(get_session)):
    return get_respuestas_por_pregunta(session, id_pregunta)

@router.put("/respuesta/{id}", response_model=RespuestaRead)
def actualizar_respuesta(id: int, respuesta_update: RespuestaUpdate, session: Session = Depends(get_session)):
    return update_respuesta(session, id, respuesta_update)

@router.delete("/respuesta/{id}", response_model=RespuestaRead)
def eliminar_respuesta(id: int, session: Session = Depends(get_session)):
    return delete_respuesta(session, id)

