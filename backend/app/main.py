from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WEB-APP API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://tu-usuario.github.io"  # reemplazar por tu GitHub Pages
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API lista y funcionando"}
