from sqlalchemy.orm import Session
from models.poliza import Poliza
from schemas import PolizaCreate, PolizaUpdate
from errors import error_already_exists

def crear_poliza(db: Session, data: PolizaCreate):
    existente = db.query(Poliza).filter(Poliza.numero_poliza == data.numero_poliza).first()
    if existente:
        error_already_exists("Póliza")
    poliza = Poliza(**data.dict())
    db.add(poliza)
    db.commit()
    db.refresh(poliza)
    return poliza

def obtener_poliza(db: Session, id: int):
    return db.query(Poliza).filter(Poliza.id == id).first()

def obtener_todas(db: Session):
    return db.query(Poliza).all()

def obtener_polizas_por_cliente(db: Session, documento: str):
    from models.cliente import Cliente
    cliente = db.query(Cliente).filter(Cliente.documento == documento).first()
    if not cliente:
        return None
    return db.query(Poliza).filter(Poliza.cliente_id == cliente.id).all()

def actualizar_poliza(db: Session, id: int, data: PolizaUpdate):
    poliza = obtener_poliza(db, id)
    if not poliza:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(poliza, k, v)
    db.commit()
    db.refresh(poliza)
    return poliza

def eliminar_poliza(db: Session, id: int):
    poliza = obtener_poliza(db, id)
    if not poliza:
        return False
    db.delete(poliza)
    db.commit()
    return True
