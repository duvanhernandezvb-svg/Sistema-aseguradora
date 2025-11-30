from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas import UsuarioCreate, UsuarioUpdate
import bcrypt

# Funciones CRUD básicas
def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Asegurar que la contraseña no exceda 72 bytes
    password = usuario.password
    if len(password.encode('utf-8')) > 72:
        password = password[:72]
    
    # Usar bcrypt directamente
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    db_usuario = Usuario(
        username=usuario.username,
        hashed_password=hashed_password,
        is_active=usuario.is_active
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()

def obtener_todos_usuarios(db: Session):
    return db.query(Usuario).all()

def actualizar_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        if usuario.password:
            # Asegurar que la nueva contraseña no exceda 72 bytes
            password = usuario.password
            if len(password.encode('utf-8')) > 72:
                password = password[:72]
            db_usuario.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if usuario.is_active is not None:
            db_usuario.is_active = usuario.is_active
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False

# Función verify_password usando bcrypt directamente
def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        # Asegurar que la contraseña no exceda 72 bytes
        if len(plain_password.encode('utf-8')) > 72:
            plain_password = plain_password[:72]
        
        # Convertir a bytes
        plain_password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
    except Exception as e:
        print(f"Error en verify_password: {e}")
        return False