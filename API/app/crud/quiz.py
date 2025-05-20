from sqlmodel import Session, select
from fastapi import HTTPException, UploadFile
from models.quiz import Quiz
from schemas.quiz import QuizCreate
from database.config import UPLOAD_FOLDER_QUIZZES
import os

def crear_quiz_service(quiz: QuizCreate, session: Session):
    nuevo_quiz = Quiz(**quiz.model_dump())
    session.add(nuevo_quiz)
    session.commit()
    session.refresh(nuevo_quiz)
    return nuevo_quiz

def leer_quizzes_service(session: Session):
    return session.exec(select(Quiz)).all()

def leer_quiz_service(quiz_id: int, session: Session):
    quiz = session.get(Quiz, quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    return quiz

def leer_quizzes_por_usuario(usuario_id: int, session: Session):
    statement = select(Quiz).where(Quiz.id_usuario == usuario_id)
    results = session.exec(statement)
    return results.all()

def actualizar_quiz_service(quiz_id: int, quiz: QuizCreate, session: Session):
    db_quiz = session.get(Quiz, quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    for key, value in quiz.dict(exclude_unset=True).items():
        setattr(db_quiz, key, value)
    session.commit()
    session.refresh(db_quiz)
    return db_quiz

def eliminar_quiz_service(quiz_id: int, session: Session):
    quiz = session.get(Quiz, quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    session.delete(quiz)
    session.commit()
    return quiz

def upload_quiz_image(session: Session, quiz_id: int, file: UploadFile):
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")

    # Guardar la imagen con un nombre único
    file_extension = file.filename.split(".")[-1]
    filename = f"quiz_{quiz_id}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER_QUIZZES, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    quiz.imagen = file_path
    session.add(quiz)
    session.commit()
    session.refresh(quiz)

    return {"message": "Imagen de quiz subida exitosamente", "image_url": file_path}