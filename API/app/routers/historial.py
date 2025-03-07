from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from database.models import Historial
from app.database.session import get_session

router = APIRouter(prefix="/historial", tags=["Historial"])

@router.post("/", response_model=Historial)
def crear_historial(historial: Historial, session: Session = Depends(get_session)):
    session.add(historial)
    session.commit()
    session.refresh(historial)
    return historial

@router.get("/", response_model=List[Historial])
def leer_historiales(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    historiales = session.exec(select(Historial).offset(skip).limit(limit)).all()
    return historiales

@router.get("/{historial_id}", response_model=Historial)
def leer_historial(historial_id: int, session: Session = Depends(get_session)):
    historial = session.get(Historial, historial_id)
    if not historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return historial

@router.put("/{historial_id}", response_model=Historial)
def actualizar_historial(historial_id: int, historial: Historial, session: Session = Depends(get_session)):
    db_historial = session.get(Historial, historial_id)
    if not db_historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    historial_data = historial.dict(exclude_unset=True)
    for key, value in historial_data.items():
        setattr(db_historial, key, value)
    session.add(db_historial)
    session.commit()
    session.refresh(db_historial)
    return db_historial

@router.delete("/{historial_id}", response_model=Historial)
def eliminar_historial(historial_id: int, session: Session = Depends(get_session)):
    historial = session.get(Historial, historial_id)
    if not historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    session.delete(historial)
    session.commit()
    return historial
