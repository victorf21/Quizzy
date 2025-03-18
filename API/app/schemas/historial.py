from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class HistorialCreate(SQLModel):
    id_usuario: Optional[int]
    num_total_preguntas: Optional[int]

class HistorialRead(SQLModel):
    id: int
    id_usuario: Optional[int]
    fecha_creacion: datetime
    num_total_preguntas: Optional[int]
