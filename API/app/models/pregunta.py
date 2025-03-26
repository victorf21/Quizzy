from sqlmodel import SQLModel, Field
from typing import Optional
import sqlalchemy as sa

class Pregunta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_quiz: Optional[int] = Field(default=None, foreign_key="quiz.id")
    descripcion: str = Field(nullable=False)
    imagen: Optional[str] = None