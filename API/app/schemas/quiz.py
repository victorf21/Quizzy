from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class QuizCreate(SQLModel):
    nombre: str
    id_usuario: Optional[int] = None
    categorias: Optional[str] = None
    num_total_preguntas: Optional[int] = None
    puntuacion: Optional[int] = None
    imagen: Optional[str] = None

class QuizRead(QuizCreate):
    id: int
    fecha_creacion: datetime

class QuizUpdate(SQLModel):
    nombre: Optional[str] = None
    categorias: Optional[str] = None
    num_total_preguntas: Optional[int] = None
    puntuacion: Optional[int] = None
    imagen: Optional[str] = None 