from sqlmodel import SQLModel, Field
from typing import Optional

class Respuesta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_pregunta: int = Field(foreign_key="pregunta.id")
    descripcion: str = Field(nullable=False)
    valido: bool = Field(nullable=False)

class RespuestaCreate(SQLModel):
    id_pregunta: int
    descripcion: str
    valido: bool

class RespuestaRead(RespuestaCreate):
    id: int

class RespuestaUpdate(SQLModel):
    descripcion: Optional[str] = None
    valido: Optional[bool] = None