from sqlmodel import SQLModel, Field
from typing import Optional
import sqlalchemy as sa

class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(nullable=False)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id")
    categorias: Optional[str] = None
    num_total_preguntas: Optional[int] = None
    fecha_creacion: Optional[str] = Field(
        sa_column=sa.Column(sa.TIMESTAMP, server_default=sa.text("CURRENT_TIMESTAMP"))
    )
    puntuacion: Optional[int] = None