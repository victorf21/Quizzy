from sqlmodel import SQLModel
from typing import Optional

class PreguntaBase(SQLModel):
    descripcion: str
    id_quiz: int

class PreguntaCreate(PreguntaBase):
    pass

class PreguntaRead(PreguntaBase):
    id: int
