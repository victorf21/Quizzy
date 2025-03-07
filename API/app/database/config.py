from sqlmodel import create_engine

# Configuración de PostgreSQL

DATABASE_URL = "postgresql://postgres:pirineus@localhost:5432/trivia_db?client_encoding=utf8"
# Crear motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)
