from django import forms
from mainSite.models import Zawody, User

class LoginForm(forms.Form):
    user_auth_dat = forms.CharField(label="Email",max_length=100, widget=forms.TextInput(attrs={'class': 'dField'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'dField'}))

class RegisterForm(forms.Form):
    BELT_CHOICES = [
        ("White", "White"),
        ("Blue", "Blue"),
        ("Purple", "Purple"),
        ("Brown", "Brown"),
        ("Black", "Black"),
        ("Red", "Red"),
    ]

    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class': 'dField'}))
    user_email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'dField'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'dField'}))
    rep_password = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(attrs={'class': 'dField'}))
    belt = forms.ChoiceField(choices=BELT_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'dField'}))    

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