from sqlmodel import SQLModel
from typing import Optional
import datetime

class QuizCreate(SQLModel):
    nombre: str
    id_usuario: Optional[int] = None
    categorias: Optional[str] = None
    num_total_preguntas: Optional[int] = None
    puntuacion: Optional[int] = None

class QuizRead(QuizCreate):
    id: int
    fecha_creacion: datetime.datetime