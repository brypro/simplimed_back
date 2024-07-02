from django.contrib import admin
from .models import Rol, Usuario, Login, Paciente, Doctor, Especialidad, DoctorEspecialidad, HistorialMedico, AtencionMedica, RecetaMedica, Examen, ConsultaExamenes, Insumo, ConsultaInsumos

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Login)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(DoctorEspecialidad)
admin.site.register(HistorialMedico)
admin.site.register(AtencionMedica)
admin.site.register(RecetaMedica)
admin.site.register(Examen)
admin.site.register(ConsultaExamenes)
admin.site.register(Insumo)
admin.site.register(ConsultaInsumos)
