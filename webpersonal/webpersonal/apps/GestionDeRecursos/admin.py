from django.contrib import admin
from webpersonal.apps.GestionDeRecursos.models import Alumno, Docente, Tutor, Curso

# Register your models here.

admin.site.register(Docente)
admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Curso)