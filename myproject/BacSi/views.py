from django.shortcuts import render, redirect
from .models import BacSi
from LoaiKham.models import LoaiKham
from PhongKham.models import PhongKham
from django.contrib.auth.decorators import login_required
@login_required
def viewBacSi(request):
    bs = BacSi.objects.all()
    lk = LoaiKham.objects.all()
    context = {'bs':bs,'lk':lk}
    return render(request, 'BacSi/QLBacSi.html', context)
@login_required
def addBacSiForm(request):
    lk = LoaiKham.objects.all()
    pk = PhongKham.objects.all()
    context = {'lk':lk, 'pk': pk}
    return render(request, 'BacSi/AddBS.html', context)
@login_required
def addBacSi(request):
    if request.method == 'POST':
        BacSi_id = request.POST['BacSi_id']
        Name = request.POST['Name']
        LoaiKham_id = request.POST['LoaiKham']
        PhongKham_id = request.POST['PhongKham']
        lk = LoaiKham.objects.get(LoaiKham_id = LoaiKham_id)
        pk = PhongKham.objects.get(PhongKham_id = PhongKham_id)
        BS = BacSi.objects.create(  BacSi_id = BacSi_id,
                                    Name = Name,
                                    LoaiKham_id = lk,
                                    PhongKham_id = pk,
                                )
        BS.save()
        return redirect('/BacSi')
    else:
        return render(request, "Lỗi")
@login_required
def FormBacSi(request, id):
    bs = BacSi.objects.get(BacSi_id = id)
    lk = LoaiKham.objects.all()
    pk = PhongKham.objects.all()
    context = {'lk':lk, 'pk': pk, 'bs': bs}
    return render(request, "BacSi/FormBS.html", context)
@login_required
def DelBacSi(request, id):
    bs = BacSi.objects.get(BacSi_id = id)
    bs.delete()
    return redirect('/BacSi')
@login_required
def EditBacSi(request):
    bs = BacSi.objects.get(BacSi_id = request.POST['ID'])
    bs.Name = request.POST['Name']
    LoaiKham_id = request.POST['LoaiKham']
    PhongKham_id = request.POST['PhongKham']
    lk = LoaiKham.objects.get(LoaiKham_id = LoaiKham_id)
    pk = PhongKham.objects.get(PhongKham_id = PhongKham_id)
    bs.LoaiKham_id = lk
    bs.PhongKham_id = pk
    bs.save()
    return redirect('/BacSi')
def Fillter(request):
    # bs= BacSi.objects.get(LoaiKham_id = request.POST['LoaiKham'])
    bs= BacSi.objects.filter(Name__contains = request.POST['Search'], LoaiKham_id = request.POST['LoaiKham'])
    lk = LoaiKham.objects.all()
    context = {'bs':bs,'lk':lk}
    return render(request, 'BacSi/QLBacSi.html', context)


