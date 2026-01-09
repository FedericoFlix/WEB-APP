from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id: int
    sic: bool
    remitto: bool
    fact: bool
    epp: bool
    visor: bool

    class Config:
        from_attributes = True

class UsuarioFlagsUpdate(BaseModel):
    sic: Optional[bool] = None
    remitto: Optional[bool] = None
    fact: Optional[bool] = None
    epp: Optional[bool] = None
    visor: Optional[bool] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
