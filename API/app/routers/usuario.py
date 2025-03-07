from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from sqlmodel import select
from database.session import get_session
from database import conn
from database.models import Usuario
from sqlalchemy.orm import Session


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario
