from sqlalchemy.orm import Session
from models.cliente import Cliente
from schemas import ClienteCreate, ClienteUpdate
from errors import error_already_exists

def crear_cliente(db: Session, data: ClienteCreate):
    existente = db.query(Cliente).filter(Cliente.documento == data.documento).first()
    if existente:
        error_already_exists("Cliente")
    cliente = Cliente(**data.dict())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def obtener_cliente(db: Session, id: int):
    return db.query(Cliente).filter(Cliente.id == id).first()

def obtener_cliente_por_documento(db: Session, documento: str):
    return db.query(Cliente).filter(Cliente.documento == documento).first()

def obtener_todos(db: Session):
    return db.query(Cliente).all()

def actualizar_cliente(db: Session, id: int, data: ClienteUpdate):
    cliente = obtener_cliente(db, id)
    if not cliente:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(cliente, k, v)
    db.commit()
    db.refresh(cliente)
    return cliente

def eliminar_cliente(db: Session, id: int):
    cliente = obtener_cliente(db, id)
    if not cliente:
        return False
    db.delete(cliente)
    db.commit()
    return True
