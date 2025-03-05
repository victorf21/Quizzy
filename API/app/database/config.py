from sqlmodel import create_engine

# Configuración de PostgreSQL

DATABASE_URL = "postgresql://postgres:root@localhost:5432/trivia_db"
# Crear motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)
