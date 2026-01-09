from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from .models import Usuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def get_user_by_email(db: AsyncSession, email: str) -> Usuario | None:
    result = await db.execute(select(Usuario).where(Usuario.email == email))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, nombre: str, email: str, password: str) -> Usuario:
    user = Usuario(
        nombre=nombre,
        email=email,
        password=hash_password(password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def update_user_flags(
    db: AsyncSession,
    user: Usuario,
    *,
    sic=None, remitto=None, fact=None, epp=None, visor=None
) -> Usuario:
    if sic is not None: user.sic = sic
    if remitto is not None: user.remitto = remitto
    if fact is not None: user.fact = fact
    if epp is not None: user.epp = epp
    if visor is not None: user.visor = visor
    await db.commit()
    await db.refresh(user)
    return user
