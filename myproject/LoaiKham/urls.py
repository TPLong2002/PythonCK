from django.urls import path
from . import views
urlpatterns = [
    path('', views.viewLoaiKham),
    path('DelLoaiKham/<int:id>', views.DelLoaiKham),
    path('EditLoaiKham', views.EditLoaiKham),
    path('FormLoaiKham', views.FormLoaiKham),
    path('AddLoaiKham', views.AddLoaiKham)
]