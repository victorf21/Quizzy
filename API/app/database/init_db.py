from database.config import engine
from sqlmodel import SQLModel
from models.usuario import Usuario
from models.historial import Historial
from models.quiz import Quiz
from models.pregunta import Pregunta
from models.respuesta import Respuesta

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Base de datos y tablas creadas correctamente")