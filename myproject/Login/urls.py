from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormLogin),
    path('Home', views.Home),
    path('Success', views.Login, name = 'Success'),
    path('Logout', views.Logout, name ='Logout'),
]