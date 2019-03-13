from django.db import models
from webpersonal.apps.GestionDeRecursos.models import Alumno, Docente, Tutor, Curso

# Create your models here.

class Permiso (models.Model):
    Asunto = models.CharField(max_length=150)
    Detalle = models.CharField(max_length=1000)
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    Docente = models.ForeignKey(Docente, null=False, blank=False, on_delete=models.CASCADE)
    Aprobado = models.BooleanField(default=False)

    def __str__(self):
        return "{0} / {1} => {2}".format(self.Asunto, self.Alumno, self.Aprobado)

