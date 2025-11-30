from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import PolizaCreate, PolizaUpdate, PolizaOut
from crud.polizas import crear_poliza, obtener_poliza, obtener_todas, actualizar_poliza, eliminar_poliza, obtener_polizas_por_cliente
from auth import get_current_user
from errors import error_not_found

router = APIRouter(prefix="/polizas", tags=["Polizas"])

@router.post("/", response_model=PolizaOut, dependencies=[Depends(get_current_user)])
def api_crear_poliza(data: PolizaCreate, db: Session = Depends(get_db)):
    return crear_poliza(db, data)

@router.get("/", response_model=list[PolizaOut], dependencies=[Depends(get_current_user)])
def api_listar_polizas(db: Session = Depends(get_db)):
    return obtener_todas(db)

@router.get("/cliente/{documento}", response_model=list[PolizaOut], dependencies=[Depends(get_current_user)])
def api_polizas_cliente(documento: str, db: Session = Depends(get_db)):
    res = obtener_polizas_por_cliente(db, documento)
    if res is None:
        error_not_found("Cliente")
    return res

@router.get("/{id}", response_model=PolizaOut, dependencies=[Depends(get_current_user)])
def api_obtener_poliza(id: int, db: Session = Depends(get_db)):
    p = obtener_poliza(db, id)
    if not p:
        error_not_found("Poliza")
    return p

@router.put("/{id}", response_model=PolizaOut, dependencies=[Depends(get_current_user)])
def api_actualizar_poliza(id: int, data: PolizaUpdate, db: Session = Depends(get_db)):
    p = actualizar_poliza(db, id, data)
    if not p:
        error_not_found("Poliza")
    return p

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def api_eliminar_poliza(id: int, db: Session = Depends(get_db)):
    ok = eliminar_poliza(db, id)
    if not ok:
        error_not_found("Poliza")
    return {"mensaje": "Poliza eliminada"}
