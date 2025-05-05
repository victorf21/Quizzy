from sqlmodel import Session, select
from fastapi import HTTPException, UploadFile
from models.pregunta import Pregunta
from schemas.pregunta import PreguntaCreate
from database.config import UPLOAD_FOLDER_PREGUNTAS
import os

def crear_pregunta_service(pregunta: PreguntaCreate, session: Session):
    nueva_pregunta = Pregunta(**pregunta.model_dump())
    session.add(nueva_pregunta)
    session.commit()
    session.refresh(nueva_pregunta)
    return nueva_pregunta

def leer_preguntas_service(session: Session):
    return session.exec(select(Pregunta)).all()

def leer_pregunta_service(pregunta_id: int, session: Session):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return pregunta

def actualizar_pregunta_service(pregunta_id: int, pregunta: PreguntaCreate, session: Session):
    db_pregunta = session.get(Pregunta, pregunta_id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    for key, value in pregunta.model_dump(exclude_unset=True).items():
        setattr(db_pregunta, key, value)
    session.commit()
    session.refresh(db_pregunta)
    return db_pregunta

def eliminar_pregunta_service(pregunta_id: int, session: Session):
    pregunta = session.get(Pregunta, pregunta_id)
    if pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    session.delete(pregunta)
    session.commit()
    return pregunta

def upload_pregunta_image(session: Session, pregunta_id: int, file: UploadFile):
    pregunta = session.get(Pregunta, pregunta_id)
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    # Guardar la imagen con un nombre único
    file_extension = file.filename.split(".")[-1]
    filename = f"pregunta_{pregunta_id}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER_PREGUNTAS, filename) 

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    pregunta.imagen = file_path
    session.add(pregunta)
    session.commit()
    session.refresh(pregunta)

    return {"message": "Imagen de pregunta subida exitosamente", "image_url": file_path}