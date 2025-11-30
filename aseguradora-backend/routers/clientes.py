from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import ClienteCreate, ClienteUpdate, ClienteOut
from crud.clientes import crear_cliente, obtener_cliente, obtener_todos, actualizar_cliente, eliminar_cliente
from auth import get_current_user
from errors import error_not_found

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteOut, dependencies=[Depends(get_current_user)])
def api_crear_cliente(data: ClienteCreate, db: Session = Depends(get_db)):
    return crear_cliente(db, data)

@router.get("/", response_model=list[ClienteOut], dependencies=[Depends(get_current_user)])
def api_listar_clientes(db: Session = Depends(get_db)):
    return obtener_todos(db)

@router.get("/{id}", response_model=ClienteOut, dependencies=[Depends(get_current_user)])
def api_obtener_cliente(id: int, db: Session = Depends(get_db)):
    cliente = obtener_cliente(db, id)
    if not cliente:
        error_not_found("Cliente")
    return cliente

@router.put("/{id}", response_model=ClienteOut, dependencies=[Depends(get_current_user)])
def api_actualizar_cliente(id: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    cli = actualizar_cliente(db, id, data)
    if not cli:
        error_not_found("Cliente")
    return cli

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def api_eliminar_cliente(id: int, db: Session = Depends(get_db)):
    ok = eliminar_cliente(db, id)
    if not ok:
        error_not_found("Cliente")
    return {"mensaje": "Cliente eliminado"}
