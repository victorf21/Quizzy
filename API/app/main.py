from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import usuario, quiz, pregunta
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

app.include_router(usuario.router)
app.include_router(quiz.router)
app.include_router(pregunta.router)