from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Poliza(Base):
    __tablename__ = "polizas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    numero_poliza = Column(String(50), unique=True, index=True, nullable=False)
    tipo = Column(String(50), nullable=False)
    placa = Column(String(20), nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    valor = Column(Integer, nullable=False)

    cliente = relationship("Cliente")
