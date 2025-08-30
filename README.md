# GHL-CALENDARIO

ghl-integration/
│
├─ backend/                           # Django + API
│   ├─ ghl_backend/                   # Proyecto Django
│   │   ├─ __init__.py
│   │   ├─ settings.py
│   │   ├─ urls.py
│   │   ├─ wsgi.py
│   │   └─ asgi.py
│   │
│   ├─ ghl/                           # App para manejar GHL
│   │   ├─ __init__.py
│   │   ├─ models.py                  # Tablas (calendarios, logs)
│   │   ├─ serializers.py             # Serializadores para JSON
│   │   ├─ views.py                   # Endpoints /ghl/ping/ y /ghl/calendars/
│   │   ├─ urls.py                    # Rutas de la app ghl
│   │   ├─ admin.py                   # Registro de modelos en admin
│   │   ├─ services/                  # Lógica de conexión a GHL
│   │   │   └─ ghl_client.py          # Cliente que maneja requests a GHL API
│   │   └─ migrations/
│   │
│   ├─ manage.py
│   └─ venv/                          # Entorno virtual
│
├─ frontend/                          # React
│   ├─ public/
│   └─ src/
│       ├─ components/
│       │   ├─ PingButton.js          # Botón "Probar Conexión con GHL"
│       │   ├─ CalendarsTable.js      # Tabla con lista de calendarios
│       │   ├─ Loader.js              # Componente de carga
│       │   └─ ErrorMessage.js        # Componente de error
│       ├─ services/
│       │   └─ api.js                 # Configuración axios para llamar al backend
│       ├─ App.js                     # App principal
│       └─ index.js                   # Punto de entrada
│
├─ .env.example                       # Variables de entorno (ejemplo)
├─ requirements.txt                   # Dependencias de Python
├─ package.json                       # Dependencias de React
└─ README.md                          # Documentación del proyecto
