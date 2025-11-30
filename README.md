 Backend Aseguradora API

## Descripción
Este backend está desarrollado en **Python** usando **FastAPI** y **PostgreSQL**.  
Está diseñado para una aseguradora y tiene una arquitectura modular con **cuatro módulos principales**: Clientes, Pólizas, Siniestros y Pagos, además de un módulo de Usuarios para autenticación y login mediante JWT.  

El backend incluye:
- CRUD completo para cada módulo.
- Autenticación con **JWT** para proteger rutas.
- Validación de datos usando **Pydantic**.
- Manejo centralizado de errores.

---

## Tecnologías utilizadas
- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Pydantic
- JWT (python-jose)
- bcrypt (para hash de contraseñas)

---

## Instalación y configuración

### 1. Clonar repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd aseguradora-backend

aseguradora-backend/
│
├─ main.py               # Punto de entrada del backend
├─ config.py             # Variables de configuración (DB y JWT)
├─ database.py           # Conexión y sesión a PostgreSQL
├─ schemas.py            # Modelos Pydantic para validación de datos
├─ errors.py             # Manejo de errores HTTP
├─ auth.py               # Autenticación JWT
├─ routers/              # Endpoints de cada módulo
│   ├─ clientes.py
│   ├─ polizas.py
│   ├─ siniestros.py
│   ├─ pagos.py
│   └─ usuario.py
├─ crud/                 # Lógica CRUD para cada módulo
│   ├─ clientes.py
│   ├─ polizas.py
│   ├─ siniestros.py
│   ├─ pagos.py
│   └─ usuario.py
└─ requirements.txt      # Dependencias Python

## Ejecutar localmente
1. Crear entorno virtual: `python -m venv .venv`
2. Activar: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar `backend/.env` con tus credenciales Postgres y JWT
5. Ejecutar: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
6. Abrir docs: http://127.0.0.1:8000/docs
