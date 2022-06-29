from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombre = models.CharField(max_length = 20, verbose_name = "Nombre del Medicamento")

    def __str__(self):
        texto = '(0) ((1))'
        return texto.format(self.nombre)

class Tratamiento(models.Model):
    dolencia = models.CharField(max_length = 20, verbose_name = "Tratamiento para")
    inicio = models.DateTimeField(max_length = 20, verbose_name = "Inicio del Tratamiento")
    fin = models.DateTimeField(max_length = 20, verbose_name = "Fin del Tratamiento")

    def __str__(self):
        texto = '(0) ((1))'
        return texto.format(self.dolencia, self.inicio, self.fin)

class Doctor(models.Model):
    nombre = models.CharField(max_length = 20, verbose_name = "Nombre del Doctor")

    def __str__(self):
        texto = '(0) ((1))'
        return texto.format(self.nombre)