from sqlmodel import Session, select
from fastapi import HTTPException
from schemas.respuesta import Respuesta, RespuestaCreate, RespuestaUpdate

def create_respuesta(session: Session, respuesta: RespuestaCreate):
    nueva_respuesta = Respuesta.model_validate(respuesta)
    session.add(nueva_respuesta)
    session.commit()
    session.refresh(nueva_respuesta)
    return nueva_respuesta

def get_respuesta(session: Session, id: int):
    respuesta = session.get(Respuesta, id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    return respuesta

def get_respuestas_por_pregunta(session: Session, id_pregunta: int):
    query = select(Respuesta).where(Respuesta.id_pregunta == id_pregunta)
    return session.exec(query).all()

def update_respuesta(session: Session, id: int, respuesta_update: RespuestaUpdate):
    respuesta = session.get(Respuesta, id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    
    respuesta_dict = respuesta_update.model_dump(exclude_unset=True)
    for key, value in respuesta_dict.items():
        setattr(respuesta, key, value)

    session.add(respuesta)
    session.commit()
    session.refresh(respuesta)
    return respuesta

def delete_respuesta(session: Session, id: int):
    respuesta = session.get(Respuesta, id)
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    
    session.delete(respuesta)
    session.commit()
    return respuesta

