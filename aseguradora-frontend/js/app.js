const API_BASE = 'http://localhost:8000';

// Auth helpers mejoradas
function getToken() { 
    return localStorage.getItem('token'); 
}

function setToken(token) { 
    localStorage.setItem('token', token); 
}

function authHeaders() {
    const token = getToken();
    const headers = {
        'Content-Type': 'application/json'
    };
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
}

// Función mejorada para hacer requests
async function apiRequest(url, options = {}) {
    const defaultOptions = {
        headers: authHeaders(),
        ...options
    };

    try {
        const response = await fetch(`${API_BASE}${url}`, defaultOptions);
        
        // Si recibimos 401, limpiar token y redirigir al login
        if (response.status === 401) {
            localStorage.removeItem('token');
            show('login');
            throw new Error('Sesión expirada. Por favor inicie sesión nuevamente.');
        }
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ detail: 'Error desconocido' }));
            throw new Error(errorData.detail || `Error ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error en la petición:', error);
        throw error;
    }
}

// Navigation
const views = {
    login: document.getElementById('view-login'),
    clients: document.getElementById('view-clients'),
    policies: document.getElementById('view-policies'),
    claims: document.getElementById('view-claims'),
    payments: document.getElementById('view-payments')
};

function show(view) {
    // Ocultar todas las vistas
    Object.values(views).forEach(v => v.classList.add('hidden'));
    views[view].classList.remove('hidden');
    
    // Actualizar el módulo actual en el header
    const moduleNames = {
        'login': 'Inicio de Sesión',
        'clients': 'Gestión de Clientes', 
        'policies': 'Gestión de Pólizas',
        'claims': 'Gestión de Siniestros',
        'payments': 'Gestión de Pagos'
    };
    
    const currentModuleElement = document.getElementById('current-module');
    if (currentModuleElement) {
        currentModuleElement.textContent = moduleNames[view] || '';
    }
    
    // Resaltar botón activo
    document.querySelectorAll('nav button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    const activeButton = document.getElementById(`nav-${view}`);
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

// Asignar eventos de navegación
document.getElementById('nav-login').onclick = () => show('login');
document.getElementById('nav-clients').onclick = () => {
    if (getToken()) {
        show('clients');
        listClients();
    } else {
        show('login');
        alert('Por favor inicie sesión primero');
    }
};
document.getElementById('nav-policies').onclick = () => {
    if (getToken()) {
        show('policies');
        listPolicies();
    } else {
        show('login');
        alert('Por favor inicie sesión primero');
    }
};
document.getElementById('nav-claims').onclick = () => {
    if (getToken()) {
        show('claims');
        listClaims();
    } else {
        show('login');
        alert('Por favor inicie sesión primero');
    }
};
document.getElementById('nav-payments').onclick = () => {
    if (getToken()) {
        show('payments');
        listPayments();
    } else {
        show('login');
        alert('Por favor inicie sesión primero');
    }
};

// LOGIN mejorado
document.getElementById('form-login').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msgElement = document.getElementById('login-msg');
    msgElement.textContent = 'Conectando...';
    msgElement.className = 'msg';

    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch(`${API_BASE}/auth/token`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Credenciales incorrectas');
        }

        const data = await response.json();
        setToken(data.access_token);
        msgElement.textContent = '¡Login exitoso!';
        msgElement.className = 'msg success';
        
        // Mostrar vista de clientes después del login
        setTimeout(() => {
            show('clients');
            listClients();
        }, 1000);

    } catch (error) {
        msgElement.textContent = `Error: ${error.message}`;
        msgElement.className = 'msg error';
    }
});

// CLIENTS - Funciones mejoradas
async function listClients() {
    try {
        const data = await apiRequest('/clientes/');
        const tbody = document.querySelector('#clients-table tbody');
        tbody.innerHTML = '';
        
        data.forEach(client => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${client.id}</td>
                <td>${client.documento}</td>
                <td>${client.nombre}</td>
                <td>${client.apellido}</td>
                <td>${client.email || ''}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        document.querySelector('#clients-table tbody').innerHTML = 
            `<tr><td colspan="5">Error: ${error.message}</td></tr>`;
    }
}

// El resto de las funciones de clients, policies, claims, payments se mantienen similares pero usando apiRequest
// [Aquí irían las demás funciones actualizadas de manera similar...]

// Inicialización
show('login');

// Verificar si ya hay token al cargar la página
if (getToken()) {
    show('clients');
    listClients();
}