from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainSite.models import Trening
from mainSite.serializers import TrainingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, AddTrainingForm

@api_view(['GET', 'POST'])
def trainings_list(request):
        if request.method == 'GET':
            user_workouts = Trening.objects
            serializer = TrainingSerializer(user_workouts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = TrainingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
    
def homeView(request):
    if request.user.is_authenticated:
        r = requests.get('http://127.0.0.1:8000/workouts', params=request.GET)
        respon = r.json()
        finalArr = []
        for x in range(len(respon)):
            if respon[x]["owner"] == request.user.id:
                finalArr.append(respon[x])
        return render(request, template_name="index.html", context={"returnData":finalArr})
    else:
        return redirect('/authenticationPage/')
    
def authView(request):
    return render(request, template_name="authPage.html")

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login_page.html', {'form': form})
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            user = User.objects.create_user(username=username1, password=password1)
            user.save()
    else:
        form = RegisterForm()
    
    return render(request, 'register_page.html', {'form': form})

def logOutView(request):
    logout(request)
    return redirect('/')

def addTrainingSite(request):
    form = AddTrainingForm(request.POST)
    if form.is_valid():
        dateOfTraining = form.cleaned_data['dateOfTraining']
        hourOfTraining = form.cleaned_data['hourOfTraining']
        trainingDuration = form.cleaned_data['trainingDuration']
        typeOfWorkout = form.cleaned_data['typeOfWorkout']
        howManyFights = form.cleaned_data['howManyFights']
        fightDuration = form.cleaned_data['fightDuration']
        breakDuration = form.cleaned_data['breakDuration']
        tiredAfter = form.cleaned_data['tiredAfter']
        injuriesAfter = form.cleaned_data['injuriesAfter']
        trening = Trening.objects.create(owner=request.user, dateOfTraining=dateOfTraining, hourOfTraining=hourOfTraining, trainingDuration=trainingDuration, typeOfWorkout=typeOfWorkout, howManyFights=howManyFights, fightDuration=fightDuration, breakDuration=breakDuration, tiredAfter=tiredAfter, injuriesAfter=injuriesAfter)
        trening.save()
    return render(request, "addPage.html", {'form': form})