from django.db import models

class Rol(models.Model):
    tipo_rol = models.CharField(max_length=255)

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=20, unique=True)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Login(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    celular = models.CharField(max_length=20)

class Doctor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=255)

class DoctorEspecialidad(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    enfermedades_previas = models.CharField(max_length=255)
    cirugias = models.CharField(max_length=255)
    alergias = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255)

class AtencionMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo_consulta = models.CharField(max_length=255)
    sintomas = models.CharField(max_length=255)

class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo_consulta = models.CharField(max_length=255)
    sintomas = models.CharField(max_length=255)
    diagnostico = models.CharField(max_length=255)

class RecetaMedica(models.Model):
    consulta = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

class Examen(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.CharField(max_length=255)
    preparacion_previa = models.CharField(max_length=255)

class ConsultaExamenes(models.Model):
    consulta = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

class Insumo(models.Model):
    nombre = models.CharField(max_length=255)
    proveedor = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    caducidad = models.DateField()
    contraindicaciones = models.CharField(max_length=255)

class ConsultaInsumos(models.Model):
    consulta = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
