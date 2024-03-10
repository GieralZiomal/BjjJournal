from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainSite.models import Trening, Zawody, CompFight
from mainSite.serializers import TrainingSerializer, ZawodySerializer, CompFightSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, AddTrainingForm, AddCompForm

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
    
@api_view(['GET', 'POST'])
def comp_list(request):
        if request.method == 'GET':
            user_competitions = Zawody.objects
            user_comp_fights = CompFight.objects
            comp_serializer = ZawodySerializer(user_competitions, many=True)
            comp_fights_serializer = CompFightSerializer(user_comp_fights, many=True)
            combined_data = {
            "competitions": comp_serializer.data,
            "comp_fights": comp_fights_serializer.data
            }
            return Response(combined_data, status=status.HTTP_200_OK)
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
        params = {'password': 'bjj4life'}
        fights_r = requests.get('http://127.0.0.1:8000/workouts', params={**request.GET, **params})
        f_respon = fights_r.json()
        comp_r = requests.get('http://127.0.0.1:8000/competitions', params={**request.GET, **params})
        c_respon = comp_r.json()
        fight_finalArr = []
        ff_arr = []
        
        for x in range(len(f_respon)):
            if f_respon[x]["owner"] == request.user.id:
                fight_finalArr.append(f_respon[x])
                
        for comp in c_respon.get("competitions", []):
            comp_fights_arr = []
            comp_finalArr = []
            print(comp)
            if comp["owner"] == request.user.id:
                comp_finalArr.append(comp)
                
            for comp_fight in c_respon.get("comp_fights", []):
                if comp_fight["owner"] == request.user.id and comp_fight["whichComp"] == comp["comp_id"]:
                    comp_fights_arr.append(comp_fight)
                    
            ff_arr.append([comp_finalArr, comp_fights_arr])
        
        return render(request, template_name="index.html", context={"returnData": fight_finalArr, "compData": ff_arr})
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
        return redirect('/')
    return render(request, "addPage.html", {'form': form})

def addCompSite(request):
    form = AddCompForm(request.POST)
    if form.is_valid():
        nameOfComp = form.cleaned_data['nameOfComp']
        dateOfComp = form.cleaned_data['dateOfComp']
        place = form.cleaned_data['place']
        compt = Zawody.objects.create(owner=request.user, nameOfComp=nameOfComp, dateOfComp=dateOfComp, place=place)
        compt.save()
        return redirect('/')
    return render(request, "addComp.html", {'form': form})