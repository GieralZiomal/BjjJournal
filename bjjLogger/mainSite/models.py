from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = {

        "no-gi" : "NO-GI",
        "gi" : "GI",

    }

FIGHT_CHOICES = {

        "Win" : "W",
        "Lose" : "L",

    }

END_CHOICES = {

        "Submission" : "SUB",
        "Points" : "PO",
        "Disqualification" : "DQ",
        "Choice" : "CHO",

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
        ordering = ['-dateOfTraining']

class Zawody(models.Model):
    owner = models.ForeignKey(User, related_name='competition', on_delete=models.CASCADE)
    nameOfComp = models.CharField(max_length=20)
    dateOfComp = models.DateField()
    place = models.IntegerField()
    
    class Meta:
       ordering = ['-dateOfComp']

class CompFight(models.Model):
    compFight_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='compFight', on_delete=models.CASCADE)
    whichComp = models.ForeignKey(Zawody, related_name='competition', on_delete=models.CASCADE)
    resultOfFight = models.CharField(max_length=10, choices=FIGHT_CHOICES)
    endOfFight = models.CharField(max_length=20, choices=END_CHOICES)