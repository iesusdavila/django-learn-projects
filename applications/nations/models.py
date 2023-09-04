from django.db import models

# Create your models here.
class Nationality(models.Model):
    name = models.CharField(max_length=100)
    cod_nat = models.CharField(max_length=3)
    population = models.IntegerField()
    #bandera = models.ImageField(upload_to='banderas/')

    def __str__(self):
        return self.nombre
