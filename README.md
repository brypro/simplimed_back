SIMPLIMED
```markdown
# Proyecto Django con Django REST Framework y Autenticación por Tokens

Este proyecto es una API RESTful construida con Django y Django REST Framework, utilizando autenticación basada en tokens.

## Requisitos

- Python 3.x
- pip (Python package installer)
- Virtualenv (opcional pero recomendado)

## Instalación

### Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### Crear y Activar un Entorno Virtual

Se recomienda crear un entorno virtual para manejar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### Instalar Dependencias

Instala las dependencias requeridas utilizando pip:

```bash
pip install -r requirements.txt
```

### Configurar la Base de Datos

Aplica las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

### Crear un Superusuario

Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en la terminal para crear el superusuario.

### Correr el Servidor de Desarrollo

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`.

## Obtener el Token de Autenticación

Para obtener un token de autenticación, utiliza el siguiente endpoint. Esto se puede hacer con herramientas como `curl` o `Postman`.

### Usando `curl`

```bash
curl -X POST -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/api/api-token-auth/
```

### Usando Postman

1. Abre Postman y crea una nueva solicitud.
2. Selecciona el método `POST`.
3. Usa la URL: `http://127.0.0.1:8000/api/api-token-auth/`
4. En la pestaña `Body`, selecciona `x-www-form-urlencoded`.
5. Añade los campos `username` y `password` con tus credenciales de superusuario.
6. Haz clic en `Send` para obtener el token.

## Usar el Token de Autenticación

Para acceder a los endpoints protegidos de la API, añade el token de autenticación en los encabezados de tus solicitudes.

### Usando `curl`

```bash
curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/roles/
```

### Usando Postman

1. Añade un nuevo encabezado en tu solicitud:
   - Key: `Authorization`
   - Value: `Token <your_token>`
2. Envía la solicitud para acceder a los recursos protegidos.

## Estructura del Proyecto

```
<nombre_del_repositorio>/
    manage.py
    <nombre_del_proyecto>/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    <nombre_de_la_aplicacion>/
        __init__.py
        admin.py
        apps.py
        models.py
        serializers.py
        tests.py
        views.py
        urls.py
    venv/  # Entorno virtual (opcional)
```

## Configuración de `settings.py`

Asegúrate de que `settings.py` esté configurado correctamente:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    '<nombre_de_la_aplicacion>',
    'django_extensions',  # Opcional para ver las URLs disponibles
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## URL Patterns

### `myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('<nombre_de_la_aplicacion>.urls')),
    path('api-token-auth/', obtain_auth_token),
]
```

### `myapp/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UsuarioViewSet, LoginViewSet, PacienteViewSet, DoctorViewSet, EspecialidadViewSet, DoctorEspecialidadViewSet, HistorialMedicoViewSet, AtencionMedicaViewSet, RecetaMedicaViewSet, ExamenViewSet, ConsultaExamenesViewSet, InsumoViewSet, ConsultaInsumosViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'logins', LoginViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'doctor_especialidades', DoctorEspecialidadViewSet)
router.register(r'historiales_medicos', HistorialMedicoViewSet)
router.register(r'atenciones_medicas', AtencionMedicaViewSet)
router.register(r'recetas_medicas', RecetaMedicaViewSet)
router.register(r'examenes', ExamenViewSet)
router.register(r'consulta_examenes', ConsultaExamenesViewSet)
router.register(r'insumos', InsumoViewSet)
router.register(r'consulta_insumos', ConsultaInsumosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## Migraciones

Recuerda siempre aplicar las migraciones después de hacer cambios en los modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Licencia

Este proyecto está licenciado bajo los términos de la licencia [MIT License](LICENSE).
```

Este README proporciona instrucciones claras para instalar, configurar y usar tu proyecto Django con autenticación basada en tokens. Asegúrate de reemplazar los `<placeholders>` con los valores correspondientes a tu proyecto.
