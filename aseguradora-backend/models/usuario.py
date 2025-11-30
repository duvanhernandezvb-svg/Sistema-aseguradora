from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"  # Cambiar a plural para consistencia
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)