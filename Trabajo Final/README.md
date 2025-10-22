# Tienda de impresión 3D — integración rápida

Archivos añadidos:

- `templates/index.html`: plantilla principal con Bootstrap.
- `myshop/views.py`: vista `index` que pasa una lista de productos de ejemplo.
- `myshop/urls.py`: rutas de la app.

Cómo integrar en tu proyecto Django existente:

1. Asegúrate de tener una app llamada `myshop` o mover `myshop/` al lugar apropiado.
2. En `settings.py` añade `myshop` a `INSTALLED_APPS` si quieres usar modelos o traducciones.
3. Configura plantillas: en `settings.py` confirma que `TEMPLATES` incluye la ruta a `templates/` o usa `BASE_DIR / 'templates'`.

Ejemplo mínimo de `TEMPLATES` (en `settings.py`):

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

4. Incluir las URLs de la app en `urls.py` del proyecto principal:

    from django.urls import path, include

    urlpatterns = [
        path('', include('myshop.urls')),
        path('admin/', admin.site.urls),
    ]

5. Asegúrate de tener las URLs de autenticación (login/logout/signup). Puedes usar `django.contrib.auth` o una app de terceros.

Comandos PowerShell para crear entorno y ejecutar servidor (ejecutar desde la carpeta del proyecto donde está `manage.py`):

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
; pip install django
; python manage.py migrate
; python manage.py runserver
```

Notas:
- `myshop/views.py` usa datos de ejemplo en memoria; para una tienda real crea modelos en `myshop/models.py` y administra productos vía admin o panel.
- Si quieres que genere todos los archivos para una app completa (models, formularios, autenticación lista), dime y lo genero.
