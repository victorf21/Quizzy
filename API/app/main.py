from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import usuario, quiz, pregunta, historial, respuesta
from fastapi.staticfiles import StaticFiles
# python -m uvicorn main:app --reload  
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar la carpeta de archivos subidos como ruta estática
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(usuario.router)
app.include_router(quiz.router)
app.include_router(pregunta.router)
app.include_router(historial.router)
app.include_router(respuesta.router)