from django.db import models

from applications.nations.models import Nationality

# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Nationality, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre