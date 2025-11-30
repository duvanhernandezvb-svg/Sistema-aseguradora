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

### Backend
- FastAPI
- Python 3.8+
- SQLite (o la base de datos que estés usando)
- Autenticación JWT

### Frontend
- HTML5
- CSS3 (Variables CSS, Grid, Flexbox)
- JavaScript (ES6+)
- Fetch API para comunicación con el backend

---
## Ejecutar localmente
1. Crear entorno virtual: `python -m venv .venv`
2. Activar: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar `backend/.env` con tus credenciales Postgres y JWT
5. Ejecutar: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
6. Abrir docs: http://127.0.0.1:8000/docs

📋 Módulos del Sistema - Aseguradora
1. Módulo de Autenticación
-Login con usuario y contraseña - Acceso seguro al sistema
-Generación de tokens JWT - Autenticación moderna y segura
-Protección de rutas privadas - Control de acceso a funcionalidades

2. Gestión de Clientes
-Crear nuevos clientes - Registro completo de información
-Consultar y actualizar información - Mantenimiento de datos
-Eliminar clientes - Gestión completa del ciclo de vida
-Listado completo - Vista general de todos los clientes

3. Gestión de Pólizas
-Creación de pólizas - Generación de nuevas pólizas de seguro
-Asociación con clientes - Vinculación póliza-cliente
-Búsqueda por documento - Consulta rápida por identificación
-Listado general - Inventario completo de pólizas

4. Gestión de Siniestros
-Registro de siniestros - Captura de incidentes reportados
-Asociación con pólizas - Relación siniestro-póliza afectada
-Consulta por cliente - Historial de siniestros por cliente
-Historial completo - Base de datos de todos los siniestros

5. Gestión de Pagos
-Registro de pagos - Control de transacciones financieras
-Control de estado (pagado/pendiente) - Seguimiento de estados de pago
-Consultas por cliente - Historial de pagos por cliente
-Reportes de pagos - Generación de informes financieros

---
6. API Endpoints
Autenticación
-POST /auth/token - Obtener token de acceso

Clientes
-GET /clientes/ - Listar todos los clientes
-POST /clientes/ - Crear nuevo cliente
-GET /clientes/{id} - Obtener cliente por ID
-PUT /clientes/{id} - Actualizar cliente
-DELETE /clientes/{id} - Eliminar cliente

Pólizas
-GET /polizas/ - Listar pólizas
-POST /polizas/ - Crear póliza
-GET /polizas/cliente/{documento} - Pólizas por cliente

Siniestros
-GET /siniestros/ - Listar siniestros
-POST /siniestros/ - Crear siniestro
-GET /siniestros/cliente/{documento} - Siniestros por cliente

Pagos
-GET /pagos/ - Listar pagos
-POST /pagos/ - Registrar pago
-GET /pagos/cliente/{documento} - Pagos por cliente
