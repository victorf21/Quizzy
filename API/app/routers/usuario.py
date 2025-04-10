from fastapi import APIRouter, Depends, Query, UploadFile, File
from database.session import get_session
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioUpdate, UsuarioLogin
from crud.usuario import *
from fastapi.responses import FileResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioRead)
def crear_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    return create_usuario(session, usuario)

@router.post("/login")
def login(usuario: UsuarioLogin, session: Session = Depends(get_session)):
    return login_usuario(session, usuario)

@router.get("/", response_model=list[UsuarioRead])
def leer_usuarios(session: Session = Depends(get_session), offset: int = 0, limit: int = Query(100, le=100)):
    return get_usuarios(session, offset, limit)

@router.get("/{usuario_id}", response_model=UsuarioRead)
def leer_usuario(usuario_id: int, session: Session = Depends(get_session)):
    return get_usuario(session, usuario_id)

@router.put("/{usuario_id}", response_model=UsuarioRead)
def actualizar_usuario(usuario_id: int, usuario_update: UsuarioUpdate, session: Session = Depends(get_session)):
    return update_usuario(session, usuario_id, usuario_update)

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    return delete_usuario(session, usuario_id)

@router.post("/{usuario_id}/avatar")
def subir_avatar(usuario_id: int, file: UploadFile = File(...), session: Session = Depends(get_session)):
    return upload_avatar(session, usuario_id, file)

@router.get("/{usuario_id}/avatar")
def obtener_avatar(usuario_id: int, session: Session = Depends(get_session)):
    usuario = get_usuario(session, usuario_id)
    
    if not usuario.avatar:
        raise HTTPException(status_code=404, detail="El usuario no tiene avatar")

    return FileResponse(usuario.avatar)