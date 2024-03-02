from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = {

        "no-gi" : "NO-GI",
        "gi" : "GI",

    }

class Trening(models.Model):
    owner = models.ForeignKey(User, related_name='training', on_delete=models.CASCADE)
    dateOfTraining = models.DateField()
    hourOfTraining = models.TimeField()
    trainingDuration = models.IntegerField()
    typeOfWorkout = models.CharField(max_length=5, choices=TYPE_CHOICES)
    howManyFights = models.IntegerField()
    fightDuration = models.IntegerField()
    breakDuration = models.IntegerField()
    tiredAfter = models.IntegerField()
    injuriesAfter = models.CharField(max_length=10)

    class Meta:
        ordering = ['dateOfTraining']