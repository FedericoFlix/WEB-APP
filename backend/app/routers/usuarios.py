from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from ..schemas import UsuarioCreate, UsuarioOut, LoginRequest, UsuarioFlagsUpdate
from ..crud import create_user, get_user_by_email, verify_password, update_user_flags

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/registro", response_model=UsuarioOut)
async def registrar_usuario(payload: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    user = await create_user(db, nombre=payload.nombre, email=payload.email, password=payload.password)
    return user

@router.post("/login", response_model=UsuarioOut)
async def login_usuario(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user

@router.patch("/flags", response_model=UsuarioOut)
async def actualizar_flags(
    email: str,
    flags: UsuarioFlagsUpdate,
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    updated = await update_user_flags(
        db, user,
        sic=flags.sic, remitto=flags.remitto, fact=flags.fact, epp=flags.epp, visor=flags.visor
    )
    return updated
