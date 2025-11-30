from sqlalchemy.orm import Session
from models.pago import Pago
from schemas import PagoCreate, PagoUpdate

def crear_pago(db: Session, data: PagoCreate):
    pago = Pago(**data.dict())
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago

def obtener_pago(db: Session, id: int):
    return db.query(Pago).filter(Pago.id == id).first()

def obtener_todos(db: Session):
    return db.query(Pago).all()

def obtener_pagos_por_cliente(db: Session, documento: str):
    from models.cliente import Cliente
    cliente = db.query(Cliente).filter(Cliente.documento == documento).first()
    if not cliente:
        return None
    return db.query(Pago).filter(Pago.cliente_id == cliente.id).all()

def actualizar_pago(db: Session, id: int, data: PagoUpdate):
    p = obtener_pago(db, id)
    if not p:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p

def eliminar_pago(db: Session, id: int):
    p = obtener_pago(db, id)
    if not p:
        return False
    db.delete(p)
    db.commit()
    return True
