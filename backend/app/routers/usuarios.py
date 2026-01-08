# backend/app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from ..crud import get_user_by_username, create_user, verify_password

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/registro")
async def registrar_usuario(username: str, password: str, db: AsyncSession = Depends(get_db)):
    existing = await get_user_by_username(db, username)
    if existing:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    user = await create_user(db, username, password)
    return {"id": user.id, "username": user.username}

@router.post("/login")
async def login_usuario(username: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db, username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    return {"message": "Login exitoso", "username": user.username}
