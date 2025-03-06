from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, Session
from database.models import Quiz
from app.database.session import get_session

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

@router.post("/", response_model=Quiz)
def crear_quiz(quiz: Quiz, session: Session = Depends(get_session)):
    session.add(quiz)
    session.commit()
    session.refresh(quiz)
    return quiz

@router.get("/", response_model=List[Quiz])
def leer_quizzes(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    quizzes = session.exec(select(Quiz).offset(skip).limit(limit)).all()
    return quizzes

@router.get("/{quiz_id}", response_model=Quiz)
def leer_quiz(quiz_id: int, session: Session = Depends(get_session)):
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    return quiz

@router.put("/{quiz_id}", response_model=Quiz)
def actualizar_quiz(quiz_id: int, quiz: Quiz, session: Session = Depends(get_session)):
    db_quiz = session.get(Quiz, quiz_id)
    if not db_quiz:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    quiz_data = quiz.dict(exclude_unset=True)
    for key, value in quiz_data.items():
        setattr(db_quiz, key, value)
    session.add(db_quiz)
    session.commit()
    session.refresh(db_quiz)
    return db_quiz

@router.delete("/{quiz_id}", response_model=Quiz)
def eliminar_quiz(quiz_id: int, session: Session = Depends(get_session)):
    quiz = session.get(Quiz, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz no encontrado")
    session.delete(quiz)
    session.commit()
    return quiz
