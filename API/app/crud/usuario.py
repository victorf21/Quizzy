import os
from sqlmodel import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate
from database.config import UPLOAD_FOLDER_USERS

def get_usuario(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def get_usuarios(session: Session, offset: int = 0, limit: int = 100):
    return session.exec(select(Usuario).offset(offset).limit(limit)).all()

def create_usuario(session: Session, usuario_data: UsuarioCreate):
    usuario_existente = session.exec(select(Usuario).where(Usuario.mail == usuario_data.mail)).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya está en uso")

    nuevo_usuario = Usuario(**usuario_data.model_dump())
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)
    return nuevo_usuario

def update_usuario(session: Session, usuario_id: int, usuario_data: UsuarioUpdate):
    usuario = get_usuario(session, usuario_id)
    for key, value in usuario_data.model_dump(exclude_unset=True).items():
        setattr(usuario, key, value)
    
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def delete_usuario(session: Session, usuario_id: int):
    usuario = get_usuario(session, usuario_id)
    session.delete(usuario)
    session.commit()
    return {"detail": "Usuario eliminado"}

def upload_avatar(session: Session, usuario_id: int, file: UploadFile):
    usuario = get_usuario(session, usuario_id)

    # Guardar la imagen con un nombre único
    file_extension = file.filename.split(".")[-1]
    filename = f"user_{usuario_id}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER_USERS, filename)

    # Guardar el archivo en la carpeta
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Actualizar la DB con la nueva ruta
    usuario.avatar = file_path
    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return {"message": "Avatar subido exitosamente", "avatar_url": file_path}