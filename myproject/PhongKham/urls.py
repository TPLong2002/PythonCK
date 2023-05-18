from django.urls import path
from . import views
urlpatterns = [
    path('', views.viewPhongKham),
    path('DelPhongKham/<int:id>', views.DelPhongKham),
    path('EditPhongKham', views.EditPhongKham),
    path('FormPhongKham', views.FormPhongKham),
    path('AddPhongKham', views.AddPhongKham)
]