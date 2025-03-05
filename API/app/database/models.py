from sqlmodel import SQLModel, Field
from typing import Optional

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mail: str = Field(unique=True, nullable=False)
    nombre: str = Field(nullable=False)
    edad: Optional[int] = None
    tipo: Optional[str] = None
    categoria: Optional[str] = None
    avatar: Optional[str] = None
    pts_x_quiz: int = Field(default=0)

class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(nullable=False)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id")
    categorias: Optional[str] = None
    num_total_preguntas: Optional[int] = None
    fecha_creacion: Optional[str] = Field(default="CURRENT_TIMESTAMP")
    puntuacion: Optional[int] = None

class Pregunta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_quiz: Optional[int] = Field(default=None, foreign_key="quiz.id")
    descripcion: str = Field(nullable=False)

class Respuesta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_pregunta: Optional[int] = Field(default=None, foreign_key="pregunta.id")
    descripcion: str = Field(nullable=False)
    valido: bool = Field(nullable=False)

class Historial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id")
    fecha_creacion: Optional[str] = Field(default="CURRENT_TIMESTAMP")
    num_total_preguntas: Optional[int] = None