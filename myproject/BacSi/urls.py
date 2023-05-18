from django.urls import path
from . import views
urlpatterns = [
    path('', views.viewBacSi),
    path('addBacSiForm', views.addBacSiForm),
    path('addBacSi', views.addBacSi),
    path('FormBacSi/<str:id>', views.FormBacSi),
    path('DelBacSi/<str:id>', views.DelBacSi),
    path('EditBacSi', views.EditBacSi, name = 'EditBacSi'),
    path('Fillter', views.Fillter, name = 'Fillter'),
]