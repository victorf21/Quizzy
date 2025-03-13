from sqlmodel import SQLModel, Field
from typing import Optional

class Respuesta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_pregunta: Optional[int] = Field(default=None, foreign_key="pregunta.id")
    descripcion: str = Field(nullable=False)
    valido: bool = Field(nullable=False)