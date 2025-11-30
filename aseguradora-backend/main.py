from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import clientes, polizas, siniestros, pagos, usuario
from auth import router as auth_router

app = FastAPI(title="Aseguradora API")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Todos los headers
)

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(auth_router)
app.include_router(clientes.router)
app.include_router(polizas.router)
app.include_router(siniestros.router)
app.include_router(pagos.router)
app.include_router(usuario.router)

@app.get("/")
def read_root():
    return {"message": "API de Aseguradora funcionando"}

# ✅ ESTA PARTE ES CRÍTICA - Mantiene el servidor ejecutándose
if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando servidor FastAPI...")
    print("📡 Servidor disponible en: http://localhost:8000")
    print("📚 Documentación en: http://localhost:8000/docs")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)