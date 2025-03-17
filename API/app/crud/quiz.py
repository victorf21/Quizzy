from sqlmodel import Session, select
from fastapi import HTTPException
from models.quiz import Quiz
from schemas.quiz import QuizCreate

def crear_quiz_service(quiz: QuizCreate, session: Session):
    nuevo_quiz = Quiz(**quiz.dict())
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
