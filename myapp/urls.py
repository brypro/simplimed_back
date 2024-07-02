from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import RolViewSet, UsuarioViewSet, LoginViewSet, PacienteViewSet, DoctorViewSet, EspecialidadViewSet, \
    DoctorEspecialidadViewSet, HistorialMedicoViewSet, ConsultaMedicaViewSet, RecetaMedicaViewSet, ExamenViewSet, \
    ConsultaExamenesViewSet, InsumoViewSet, ConsultaInsumosViewSet, AtencionMedicaViewSet

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
router.register(r'consultas_medicas', ConsultaMedicaViewSet)
router.register(r'recetas_medicas', RecetaMedicaViewSet)
router.register(r'examenes', ExamenViewSet)
router.register(r'consulta_examenes', ConsultaExamenesViewSet)
router.register(r'insumos', InsumoViewSet)
router.register(r'consulta_insumos', ConsultaInsumosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
