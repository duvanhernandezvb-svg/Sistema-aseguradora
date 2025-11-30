from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    documento: str = Field(..., example="12345678")
    nombre: str
    apellido: str
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None

class ClienteOut(ClienteBase):
    id: int
    class Config:
        from_attributes = True

class PagoBase(BaseModel):
    cliente_id: int
    poliza_id: int
    fecha_pago: date
    valor_pagado: int
    pagado: bool = False

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    fecha_pago: Optional[date] = None
    valor_pagado: Optional[int] = None
    pagado: Optional[bool] = None

class PagoOut(PagoBase):
    id: int
    class Config:
        from_attributes = True

class PolizaBase(BaseModel):
    cliente_id: int
    numero_poliza: str
    tipo: str
    placa: Optional[str] = None
    fecha_inicio: date
    fecha_fin: date
    valor: int

class PolizaCreate(PolizaBase):
    pass

class PolizaUpdate(BaseModel):
    tipo: Optional[str] = None
    placa: Optional[str] = None
    fecha_fin: Optional[date] = None
    valor: Optional[int] = None

class PolizaOut(PolizaBase):
    id: int
    class Config:
        from_attributes = True

class SiniestroBase(BaseModel):
    cliente_id: int
    poliza_id: int
    fecha: date
    descripcion: str

class SiniestroCreate(SiniestroBase):
    pass

class SiniestroUpdate(BaseModel):
    descripcion: Optional[str] = None
    estado: Optional[str] = None

class SiniestroOut(SiniestroBase):
    id: int
    estado: Optional[str]
    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    username: str
    is_active: bool = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    password: str | None = None
    is_active: bool | None = None

class UsuarioOut(UsuarioBase):
    id: int
    class Config:
        from_attributes = True

# Agregar al final de schemas.py
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None