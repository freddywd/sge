from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Docente(models.Model):
    Apellidos = models.CharField(max_length=100)
    Nombres = models.CharField(max_length=100)
    Documento = models.CharField(max_length=11)
    Usuario = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=None)

    def NombreCompleto(self):
        return "{0}, {1}".format(self.Apellidos, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):
    Nombre = models.CharField(max_length=100)
    Sala = models.CharField(max_length=10)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Sala)

class Tutor (models.Model):
    Apellidos = models.CharField(max_length=100)
    Nombres = models.CharField(max_length=100)
    Documento = models.CharField(max_length=11)
    PARENTESCOS = (('P', 'Padre'), ('M', 'Madre'), ('T', 'Tío/a'), ('A', 'Abuelo/a'), ('H', 'Hermano/a'), ('O', 'Otro'))
    Parentesco = models.CharField(max_length=1, choices=PARENTESCOS, default='P')
    Usuario = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=None)

    def NombreCompleto(self):
        return "{0}, {1}".format(self.Apellidos, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()


class Alumno(models.Model):
    Apellidos = models.CharField(max_length=100)
    Nombres = models.CharField(max_length=100)
    Documento = models.CharField(max_length=11)
    FechaDeNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='m')
    Tutores = models.ManyToManyField(Tutor)
    Usuario = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, default=None)

    def NombreCompleto(self):
        return "{0}, {1}".format(self.Apellidos, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()