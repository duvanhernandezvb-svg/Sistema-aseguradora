from sqlalchemy.orm import Session
from models.siniestro import Siniestro
from schemas import SiniestroCreate, SiniestroUpdate

def crear_siniestro(db: Session, data: SiniestroCreate):
    s = Siniestro(**data.dict())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def obtener_siniestro(db: Session, id: int):
    return db.query(Siniestro).filter(Siniestro.id == id).first()

def obtener_todos(db: Session):
    return db.query(Siniestro).all()

def obtener_siniestros_por_cliente(db: Session, documento: str):
    from models.cliente import Cliente
    cliente = db.query(Cliente).filter(Cliente.documento == documento).first()
    if not cliente:
        return None
    return db.query(Siniestro).filter(Siniestro.cliente_id == cliente.id).all()

def actualizar_siniestro(db: Session, id: int, data: SiniestroUpdate):
    s = obtener_siniestro(db, id)
    if not s:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(s, k, v)
    db.commit()
    db.refresh(s)
    return s

def eliminar_siniestro(db: Session, id: int):
    s = obtener_siniestro(db, id)
    if not s:
        return False
    db.delete(s)
    db.commit()
    return True
