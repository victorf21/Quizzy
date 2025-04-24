from sqlmodel import create_engine
import os
# Configuración de PostgreSQL

DATABASE_URL = "postgresql://postgres:pirineus@localhost:5432/trivia_db?client_encoding=utf8"
# Crear motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

UPLOAD_FOLDER = "uploads"
UPLOAD_FOLDER_USERS = os.path.join(UPLOAD_FOLDER, "users") 
UPLOAD_FOLDER_QUIZZES = os.path.join(UPLOAD_FOLDER, "quizzes")
UPLOAD_FOLDER_PREGUNTAS = os.path.join(UPLOAD_FOLDER, "preguntas")

os.makedirs(UPLOAD_FOLDER_USERS, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_QUIZZES, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_PREGUNTAS, exist_ok=True)