# backend/app/crud.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Usuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(Usuario).where(Usuario.username == username))
    return result.scalars().first()

async def create_user(db: AsyncSession, username: str, password: str):
    user = Usuario(username=username, password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
