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
    path('addComp/', views.addCompSite, name="Add-Comp-View"),
]