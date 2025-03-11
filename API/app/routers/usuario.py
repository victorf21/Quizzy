from fastapi import APIRouter, Depends, Query, HTTPException
from database.session import get_session
from database.models import Usuario
from sqlalchemy.orm import Session
from sqlmodel import select

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.get("/")
def leer_usuarios(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(100, le=100),
) -> list[Usuario]:
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return usuarios