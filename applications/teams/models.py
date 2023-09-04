from django.db import models

from applications.leagues.models import League
from applications.nations.models import Nationality

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    country = models.ForeignKey(Nationality, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre