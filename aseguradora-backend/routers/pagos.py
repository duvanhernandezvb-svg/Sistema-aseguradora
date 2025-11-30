from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import PagoCreate, PagoUpdate, PagoOut
from crud.pagos import crear_pago, obtener_pago, obtener_todos, actualizar_pago, eliminar_pago, obtener_pagos_por_cliente
from auth import get_current_user
from errors import error_not_found

router = APIRouter(prefix="/pagos", tags=["Pagos"])

@router.post("/", response_model=PagoOut, dependencies=[Depends(get_current_user)])
def api_crear_pago(data: PagoCreate, db: Session = Depends(get_db)):
    return crear_pago(db, data)

@router.get("/", response_model=list[PagoOut], dependencies=[Depends(get_current_user)])
def api_listar_pagos(db: Session = Depends(get_db)):
    return obtener_todos(db)

@router.get("/cliente/{documento}", response_model=list[PagoOut], dependencies=[Depends(get_current_user)])
def api_pagos_cliente(documento: str, db: Session = Depends(get_db)):
    res = obtener_pagos_por_cliente(db, documento)
    if res is None:
        error_not_found("Cliente")
    return res

@router.get("/{id}", response_model=PagoOut, dependencies=[Depends(get_current_user)])
def api_obtener_pago(id: int, db: Session = Depends(get_db)):
    p = obtener_pago(db, id)
    if not p:
        error_not_found("Pago")
    return p

@router.put("/{id}", response_model=PagoOut, dependencies=[Depends(get_current_user)])
def api_actualizar_pago(id: int, data: PagoUpdate, db: Session = Depends(get_db)):
    p = actualizar_pago(db, id, data)
    if not p:
        error_not_found("Pago")
    return p

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def api_eliminar_pago(id: int, db: Session = Depends(get_db)):
    ok = eliminar_pago(db, id)
    if not ok:
        error_not_found("Pago")
    return {"mensaje": "Pago eliminado"}
