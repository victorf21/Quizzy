from sqlmodel import SQLModel, Field
from typing import Optional

class UsuarioBase(SQLModel):
    mail: str = Field(unique=True, nullable=False)
    nombre: str = Field(nullable=False)
    edad: Optional[int] = None
    tipo: Optional[str] = None
    categoria: Optional[str] = None
    avatar: Optional[str] = None
    pts_x_quiz: int = Field(default=0)

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioRead(UsuarioBase):
    id: int

class UsuarioUpdate(SQLModel):
    mail: Optional[str] = None
    nombre: Optional[str] = None
    edad: Optional[int] = None
    tipo: Optional[str] = None
    categoria: Optional[str] = None
    avatar: Optional[str] = None
    pts_x_quiz: Optional[int] = None