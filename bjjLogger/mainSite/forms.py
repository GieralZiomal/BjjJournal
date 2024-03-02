from django import forms

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