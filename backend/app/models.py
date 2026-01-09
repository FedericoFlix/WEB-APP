from sqlalchemy import Column, Integer, String, Boolean
from .db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # hash
    sic = Column(Boolean, default=False, nullable=False)
    remitto = Column(Boolean, default=False, nullable=False)
    fact = Column(Boolean, default=False, nullable=False)
    epp = Column(Boolean, default=False, nullable=False)
    visor = Column(Boolean, default=False, nullable=False)
