from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from crud.usuario import (
    crear_usuario, 
    obtener_usuario, 
    obtener_todos_usuarios, 
    actualizar_usuario, 
    eliminar_usuario,
    obtener_usuario_por_username
)
from schemas import UsuarioCreate, UsuarioUpdate, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
def api_crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = obtener_usuario_por_username(db, data.username)
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="El nombre de usuario ya existe"
        )
    return crear_usuario(db, data)

@router.get("/", response_model=list[UsuarioOut])
def api_listar_usuarios(
    db: Session = Depends(get_db),
    current_user: UsuarioOut = Depends(get_current_user)
):
    return obtener_todos_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioOut)
def api_obtener_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    current_user: UsuarioOut = Depends(get_current_user)
):
    usuario = obtener_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioOut)
def api_actualizar_usuario(
    usuario_id: int, 
    data: UsuarioUpdate, 
    db: Session = Depends(get_db),
    current_user: UsuarioOut = Depends(get_current_user)
):
    usuario = actualizar_usuario(db, usuario_id, data)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{usuario_id}")
def api_eliminar_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    current_user: UsuarioOut = Depends(get_current_user)
):
    success = eliminar_usuario(db, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}
    return {"mensaje": "Usuario eliminado"}

