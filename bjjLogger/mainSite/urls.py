from django.urls import path
from mainSite import views

urlpatterns = [
    path('workouts/', views.trainings_list),
    path('competitions/', views.comp_list),
    path('', views.homeView, name="Home-Page"),
    path('authenticationPage/', views.authView, name="Auth-Page"),
    path('register/', views.registerView, name="Register-Page"),
    path('login/', views.loginView, name="Login-Page"),
    path('logout/', views.logOutView, name="Log-Out-View"),
    path('addWorkout/', views.addTrainingSite, name="Add-Training-View"),
    path('comp/add', views.addCompSite, name="Add-Comp-View"),
    path('fight/add', views.addFightView, name="add_fight_view"),
    path('settings/', views.SettingsView, name="Settings-View"),
    path('settings/changebelt', views.ChangeBeltView, name="Change-Belt-View"),
]