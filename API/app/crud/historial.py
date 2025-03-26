from sqlmodel import Session, select
from fastapi import HTTPException
from models.historial import Historial
from schemas.historial import HistorialCreate

def crear_historial_service(historial: HistorialCreate, session: Session):
    nuevo_historial = Historial(**historial.model_dump())
    session.add(nuevo_historial)
    session.commit()
    session.refresh(nuevo_historial)
    return nuevo_historial

def leer_historiales_service(session: Session):
    return session.exec(select(Historial)).all()

def leer_historial_service(historial_id: int, session: Session):
    historial = session.get(Historial, historial_id)
    if historial is None:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return historial

def eliminar_historial_service(historial_id: int, session: Session):
    historial = session.get(Historial, historial_id)
    if historial is None:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    session.delete(historial)
    session.commit()
    return historial

def actualizar_historial(historial_id: int, historial_data: HistorialCreate, session: Session):
    historial = session.get(Historial, historial_id)
    if historial is None:
        raise HTTPException(status_code=404, detail="Historial no encontrado")

    historial_data_dict = historial_data.model_dump()
    for key, value in historial_data_dict.items():
        setattr(historial, key, value)

    session.add(historial)
    session.commit()
    session.refresh(historial)
    return historial