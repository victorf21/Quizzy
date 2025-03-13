from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from database.session import get_session
from models.quiz import Quiz
from schemas.quiz import QuizCreate, QuizRead

router = APIRouter(prefix="/quizes", tags=["Quizes"])

@router.post("/", response_model=QuizRead)
def crear_quiz(quiz: QuizCreate, session: Session = Depends(get_session)):
    nuevo_quiz = Quiz(**quiz.dict())
    session.add(nuevo_quiz)
    session.commit()
    session.refresh(nuevo_quiz)
    return nuevo_quiz

@router.get("/", response_model=List[QuizRead])
def leer_quizzes(session: Session = Depends(get_session)):
    quizzes = session.exec(select(Quiz)).all()
    return quizzes

@router.get("/{quiz_id}", response_model=QuizRead)
def leer_quiz(quiz_id: int, session: Session = Depends(get_session)):
    quiz = session.get(Quiz, quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    return quiz

@router.put("/{quiz_id}", response_model=QuizRead)
def actualizar_quiz(quiz_id: int, quiz: QuizCreate, session: Session = Depends(get_session)):
    db_quiz = session.get(Quiz, quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    for key, value in quiz.dict(exclude_unset=True).items():
        setattr(db_quiz, key, value)
    session.commit()
    session.refresh(db_quiz)
    return db_quiz

@router.delete("/{quiz_id}", response_model=QuizRead)
def eliminar_quiz(quiz_id: int, session: Session = Depends(get_session)):
    quiz = session.get(Quiz, quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    session.delete(quiz)
    session.commit()
    return quiz
