from django.db import models

from applications.teams.models import Team
from applications.nations.models import Nationality

# Create your models here.
class Player(models.Model):
    first_name = models.CharField("First Name",max_length=50)
    last_name = models.CharField("Last name",max_length=50)
    birthdate = models.DateField("Birthdate")
    position = models.CharField("Position",max_length=50)
    weight = models.DecimalField("Weight",max_digits=4, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    nation = models.ForeignKey(Nationality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.nombre