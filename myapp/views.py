from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Rol, Usuario, Login, Paciente, Doctor, Especialidad, DoctorEspecialidad, HistorialMedico, \
    AtencionMedica, RecetaMedica, Examen, ConsultaExamenes, Insumo, ConsultaInsumos, ConsultaMedica
from .serializers import RolSerializer, UsuarioSerializer, LoginSerializer, PacienteSerializer, DoctorSerializer, \
    EspecialidadSerializer, DoctorEspecialidadSerializer, HistorialMedicoSerializer, ConsultaMedicaSerializer, \
    RecetaMedicaSerializer, ExamenSerializer, ConsultaExamenesSerializer, InsumoSerializer, ConsultaInsumosSerializer, \
    AtencionMedicaSerializer, UserSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorEspecialidadViewSet(viewsets.ModelViewSet):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer
    permission_classes = [permissions.IsAuthenticated]

class AtencionMedicaViewSet(viewsets.ModelViewSet):
    queryset = AtencionMedica.objects.all()
    serializer_class = AtencionMedicaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    permission_classes = [permissions.IsAuthenticated]
class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsultaExamenesViewSet(viewsets.ModelViewSet):
    queryset = ConsultaExamenes.objects.all()
    serializer_class = ConsultaExamenesSerializer
    permission_classes = [permissions.IsAuthenticated]

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsultaInsumosViewSet(viewsets.ModelViewSet):
    queryset = ConsultaInsumos.objects.all()
    serializer_class = ConsultaInsumosSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]