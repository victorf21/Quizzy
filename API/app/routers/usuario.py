from fastapi import APIRouter, Depends, Query, HTTPException
from database.session import get_session
from ..models.usuario import Usuario
from sqlalchemy.orm import Session
from sqlmodel import select
from schemas.usuario import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/create_usuario", response_model=UsuarioRead)
def crear_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    nuevo_usuario = Usuario(**usuario.model_dump()) 
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/")
def leer_usuarios(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(100, le=100),
) -> list[Usuario]:
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return usuarios