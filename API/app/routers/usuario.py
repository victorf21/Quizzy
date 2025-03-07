from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from sqlmodel import select
from API.app.database.session import get_session
from app.database import conn
from database.models import Usuario
from sqlalchemy.orm import Session


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
