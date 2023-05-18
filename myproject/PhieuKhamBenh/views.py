from django.shortcuts import render
from django.http import HttpResponse
from LoaiKham.models import LoaiKham
from PhongKham.models import PhongKham
from BacSi.models import BacSi

# Create your views here.
def index(request):
    # return HttpResponse("Xin Chào")
    context = {'LoaiKham':LoaiKham.objects.all(), 
               'PhongKham': PhongKham.objects.all(),
                'BacSi': BacSi.objects.all(),
            }
    return render(request, 'PhieuKhamBenh/home.html', context)