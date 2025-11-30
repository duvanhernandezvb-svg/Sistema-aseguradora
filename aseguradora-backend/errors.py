from fastapi import HTTPException, status

def error_unauthorized():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado. Token inválido o ausente.",
        headers={"WWW-Authenticate": "Bearer"}
    )

def error_not_found(entity: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} no encontrado."
    )

def error_invalid_data(detail: str = "Datos inválidos o incompletos."):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )

def error_internal(detail: str = "Error interno del servidor."):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=detail
    )

def error_already_exists(entity: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"{entity} ya existe."
    )
