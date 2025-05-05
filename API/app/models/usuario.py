from sqlmodel import SQLModel, Field
from typing import Optional

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mail: str = Field(unique=True, nullable=False)
    nombre: str = Field(nullable=False)
    password: str = Field(nullable=False)
    edad: Optional[int] = None
    tipo: Optional[str] = None
    categoria: Optional[str] = None
    avatar: Optional[str] = None
    pts_x_quiz: int = Field(default=0)