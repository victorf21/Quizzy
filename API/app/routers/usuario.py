from fastapi import APIRouter, Depends
from database.session import get_session
from database.models import Usuario
from sqlalchemy.orm import Session


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario
