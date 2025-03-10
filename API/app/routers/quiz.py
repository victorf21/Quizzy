from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from sqlmodel import select
from database.session import get_session
from database import conn
from database.models import Quiz
from sqlalchemy.orm import Session

router = APIRouter(prefix="/quizes", tags=["Quizes"])

@router.post("/", response_model=Quiz)
def crear_quiz(quiz: Quiz, session: Session = Depends(get_session)):
    session.add(quiz)
    session.commit()
    session.refresh(quiz)
    return quiz