from django.db import models

from applications.nations.models import Nationality

# Create your models here.
class League(models.Model):

    name = models.CharField("Name",max_length=100)
    country = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    num_teams = models.PositiveIntegerField("Number of teams", default=0)

    def __str__(self):
        return self.name