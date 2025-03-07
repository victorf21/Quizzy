from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import usuario
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