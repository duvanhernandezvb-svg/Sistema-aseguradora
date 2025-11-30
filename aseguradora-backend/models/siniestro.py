from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database import Base

class Siniestro(Base):
    __tablename__ = "siniestros"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    poliza_id = Column(Integer, ForeignKey("polizas.id"), nullable=False)

    fecha = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=False)
    estado = Column(String(50), default="En revisión")

    cliente = relationship("Cliente")
    poliza = relationship("Poliza")
