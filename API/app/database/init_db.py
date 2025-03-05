from app.database.config import engine
from .models import SQLModel

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Base de datos y tablas creadas correctamente")
