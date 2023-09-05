from django.db import models

from applications.nations.models import Nationality

# Create your models here.
class League(models.Model):
    LEAGUE_CHOICES = (
        (1, '12'),
        (2, '16'),
        (3, '20'),
        (4, '24'),
        (5, '28'),
        (6, '32'),
        (7, '36'),
        (8, '40'),
    )

    name = models.CharField("Name",max_length=100)
    country = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    number_teams = models.IntegerField("Number of teams",max_length=1, choices=LEAGUE_CHOICES)

    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'
        ordering = ['name']
        unique_together = ('name', 'country')

    def __str__(self):
        return self.nombre