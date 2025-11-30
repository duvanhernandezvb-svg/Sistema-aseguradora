# recreate_admin.py
from database import SessionLocal
from models.usuario import Usuario
import bcrypt

def recrear_admin():
    db = SessionLocal()
    try:
        # Eliminar usuario admin existente si existe
        usuario_existente = db.query(Usuario).filter(Usuario.username == "admin").first()
        if usuario_existente:
            db.delete(usuario_existente)
            db.commit()
            print("✅ Usuario admin anterior eliminado")
        
        # Crear nuevo usuario admin con contraseña segura
        password = "admin123"
        if len(password.encode('utf-8')) > 72:
            password = password[:72]
            
        # Usar bcrypt directamente
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        usuario = Usuario(
            username="admin",
            hashed_password=hashed_password,
            is_active=True
        )
        
        db.add(usuario)
        db.commit()
        print("✅ Nuevo usuario admin creado exitosamente")
        print(f"📝 Credenciales: admin / admin123")
        print(f"🔐 Hash generado: {hashed_password[:50]}...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    recrear_admin()