from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError
from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_MINUTES
from database import get_db
from crud.usuario import obtener_usuario_por_username, verify_password
from schemas import Token

# Configuración OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    try:
        print(f"🔐 Intentando login para usuario: {form_data.username}")
        
        usuario = obtener_usuario_por_username(db, form_data.username)
        
        if not usuario:
            print("❌ Usuario no encontrado")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña inválidos",
            )
        
        print(f"✅ Usuario encontrado: {usuario.username}")
        
        # Verificar contraseña con manejo de errores
        try:
            password_valid = verify_password(form_data.password, usuario.hashed_password)
        except Exception as e:
            print(f"❌ Error verificando contraseña: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno al verificar contraseña"
            )
        
        if not password_valid:
            print("❌ Contraseña incorrecta")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña inválidos",
            )
        
        print("✅ Contraseña correcta")
        
        # Crear token
        access_token_expires = timedelta(minutes=JWT_EXPIRATION_MINUTES)
        expire = datetime.utcnow() + access_token_expires
        
        to_encode = {"sub": usuario.username, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        
        print("✅ Token generado exitosamente")
        return {"access_token": encoded_jwt, "token_type": "bearer"}
        
    except HTTPException:
        # Re-lanzar excepciones HTTP que ya manejamos
        raise
    except Exception as e:
        print(f"🔥 ERROR inesperado en login: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

# 🔥 ESTA FUNCIÓN DEBE ESTAR DEFINIDA - ES LA QUE FALTA
def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError as e:
        print(f"❌ Error JWT: {e}")
        raise credentials_exception
    
    user = obtener_usuario_por_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user