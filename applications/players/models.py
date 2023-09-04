from django.db import models

from applications.teams.models import Team
from applications.nations.models import Nationality

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    position = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nationality, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre