from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session
from database.session import get_session
from schemas.historial import HistorialCreate, HistorialRead
from crud.historial import crear_historial_service, leer_historiales_service, leer_historial_service, eliminar_historial_service

router = APIRouter(prefix="/historial", tags=["Historial"])

@router.post("/", response_model=HistorialRead)
def crear_historial(historial: HistorialCreate, session: Session = Depends(get_session)):
    return crear_historial_service(historial, session)

@router.get("/", response_model=List[HistorialRead])
def leer_historiales(session: Session = Depends(get_session)):
    return leer_historiales_service(session)

@router.get("/{historial_id}", response_model=HistorialRead)
def leer_historial(historial_id: int, session: Session = Depends(get_session)):
    return leer_historial_service(historial_id, session)

@router.delete("/{historial_id}", response_model=HistorialRead)
def eliminar_historial(historial_id: int, session: Session = Depends(get_session)):
    return eliminar_historial_service(historial_id, session)
