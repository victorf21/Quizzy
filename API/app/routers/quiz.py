from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from database.session import get_session
from models.quiz import Quiz
from schemas.quiz import QuizCreate, QuizRead
from crud.quiz import *

router = APIRouter(prefix="/quizes", tags=["Quizes"])

@router.post("/", response_model=QuizRead)
def crear_quiz(quiz: QuizCreate, session: Session = Depends(get_session)):
    return crear_quiz_service(quiz, session)

@router.get("/", response_model=List[QuizRead])
def leer_quizzes(session: Session = Depends(get_session)):
    return leer_quizzes_service(session)

@router.get("/{quiz_id}", response_model=QuizRead)
def leer_quiz(quiz_id: int, session: Session = Depends(get_session)):
    return leer_quiz_service(quiz_id, session)

@router.get("/quiz/{usuario_id}", response_model=List[QuizRead])
def leer_quizzes_por_usuario(usuario_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Quiz).where(Quiz.id_usuario == usuario_id)).all()

@router.put("/{quiz_id}", response_model=QuizRead)
def actualizar_quiz(quiz_id: int, quiz: QuizCreate, session: Session = Depends(get_session)):
    return actualizar_quiz_service(quiz_id, quiz, session)

@router.delete("/{quiz_id}", response_model=QuizRead)
def eliminar_quiz(quiz_id: int, session: Session = Depends(get_session)):
    return eliminar_quiz_service(quiz_id, session)

@router.post("/{quiz_id}/imagen")
def subir_imagen_quiz(quiz_id: int, file: UploadFile, session: Session = Depends(get_session)):
    return upload_quiz_image(session, quiz_id, file)