# backend/app/models.py
from sqlalchemy import Column, Integer, String
from .db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)  # contraseña hasheada
