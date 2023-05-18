from django.urls import path
from . import views
urlpatterns = [
    path('', views.ViewBenhNhan),
    path('FormBenhNhan/<str:id>', views.FormBenhNhan),
    path('EditBenhNhan', views.EditBenhNhan, name = 'EditBenhNhan'),
    path('FormAddBN', views.FormAddBN, name = 'FormAddBN'),
    path('AddBN', views.AddBN, name = 'AddBN'),
    path('DelBN/<str:id>', views.DelBN),
    path('Fillter', views.Fillter, name = 'Fillter'),
]