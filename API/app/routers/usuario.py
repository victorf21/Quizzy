from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from sqlmodel import select
from API.app.database.session import get_session
from app.database import conn
from database.models import Usuario
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.get("/", response_model=List[Usuario])
def leer_usuarios(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario).offset(skip).limit(limit)).all()
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def leer_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, usuario: Usuario, session: Session = Depends(get_session)):
    db_usuario = session.get(Usuario, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_data = usuario.dict(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(db_usuario, key, value)
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario

@router.delete("/{usuario_id}", response_model=Usuario)
def eliminar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(usuario)
    session.commit()
    return usuario