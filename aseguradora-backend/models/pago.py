from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    poliza_id = Column(Integer, ForeignKey("polizas.id"), nullable=False)

    fecha_pago = Column(Date, nullable=False)
    valor_pagado = Column(Integer, nullable=False)
    pagado = Column(Boolean, default=False)

    cliente = relationship("Cliente")
    poliza = relationship("Poliza")
