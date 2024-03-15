from django import forms
from mainSite.models import Zawody

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTrainingForm(forms.Form):
    TYPE_CHOICES = {

        ("no-gi","NO-GI"),
        ("gi","GI")

    }
    dateOfTraining = forms.DateField()
    hourOfTraining = forms.TimeField()
    trainingDuration = forms.IntegerField()
    typeOfWorkout = forms.ChoiceField(choices=TYPE_CHOICES)
    howManyFights = forms.IntegerField()
    fightDuration = forms.IntegerField()
    breakDuration = forms.IntegerField()
    tiredAfter = forms.IntegerField()
    injuriesAfter = forms.CharField(max_length=10)

class AddCompForm(forms.Form):
    nameOfComp = forms.CharField(max_length=20)
    dateOfComp = forms.DateField()
    place = forms.IntegerField()

class AddFightForm(forms.Form):
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
    resultOfFight = forms.ChoiceField(choices=FIGHT_CHOICES)
    endOfFight = forms.ChoiceField(choices=END_CHOICES)