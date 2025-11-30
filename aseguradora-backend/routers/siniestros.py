from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import SiniestroCreate, SiniestroUpdate, SiniestroOut
from crud.siniestros import crear_siniestro, obtener_siniestro, obtener_todos, actualizar_siniestro, eliminar_siniestro, obtener_siniestros_por_cliente
from auth import get_current_user
from errors import error_not_found

router = APIRouter(prefix="/siniestros", tags=["Siniestros"])

@router.post("/", response_model=SiniestroOut, dependencies=[Depends(get_current_user)])
def api_crear_siniestro(data: SiniestroCreate, db: Session = Depends(get_db)):
    return crear_siniestro(db, data)

@router.get("/", response_model=list[SiniestroOut], dependencies=[Depends(get_current_user)])
def api_listar_siniestros(db: Session = Depends(get_db)):
    return obtener_todos(db)

@router.get("/cliente/{documento}", response_model=list[SiniestroOut], dependencies=[Depends(get_current_user)])
def api_siniestros_cliente(documento: str, db: Session = Depends(get_db)):
    res = obtener_siniestros_por_cliente(db, documento)
    if res is None:
        error_not_found("Cliente")
    return res

@router.get("/{id}", response_model=SiniestroOut, dependencies=[Depends(get_current_user)])
def api_obtener_siniestro(id: int, db: Session = Depends(get_db)):
    s = obtener_siniestro(db, id)
    if not s:
        error_not_found("Siniestro")
    return s

@router.put("/{id}", response_model=SiniestroOut, dependencies=[Depends(get_current_user)])
def api_actualizar_siniestro(id: int, data: SiniestroUpdate, db: Session = Depends(get_db)):
    s = actualizar_siniestro(db, id, data)
    if not s:
        error_not_found("Siniestro")
    return s

@router.delete("/{id}", dependencies=[Depends(get_current_user)])
def api_eliminar_siniestro(id: int, db: Session = Depends(get_db)):
    ok = eliminar_siniestro(db, id)
    if not ok:
        error_not_found("Siniestro")
    return {"mensaje": "Siniestro eliminado"}
