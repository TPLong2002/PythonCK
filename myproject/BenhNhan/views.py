from django.shortcuts import render, redirect
from .models import BenhNhan
from BacSi.models import BacSi
from LoaiKham.models import LoaiKham
from PhongKham.models import PhongKham
from django.contrib.auth.decorators import login_required
@login_required
def ViewBenhNhan(request):
    bn = BenhNhan.objects.all()
    lk = LoaiKham.objects.all()
    bs = BacSi.objects.all()
    context = {'bn':bn, 'lk': lk, 'bs' : bs}
    return render(request, 'BenhNhan/ViewBenhNhan.html', context)
@login_required
def FormBenhNhan(request, id):
    bs = BacSi.objects.all()
    lk = LoaiKham.objects.all()
    pk = PhongKham.objects.all()
    bn = BenhNhan.objects.get(BenhNhan_id = id)
    context = {'bn':bn, 'bs':bs, 'lk':lk, 'pk':pk}
    return render(request, 'BenhNhan/FormBenhNhan.html', context)
@login_required
def EditBenhNhan(request):
    bn = BenhNhan.objects.get(BenhNhan_id = request.POST['ID'])
    bn.Name = request.POST['Name']
    bn.Age = request.POST['Age']
    bn.Gender = request.POST['Gender']
    bn.LoaiKham_id = LoaiKham.objects.get(LoaiKham_id = request.POST['LoaiKham'])
    bn.BSPhuTrach = BacSi.objects.get(BacSi_id = request.POST['BSPhuTrach'])
    bn.PhongKham_id = PhongKham.objects.get(PhongKham_id = request.POST['PhongKham'])
    # bn.LoaiKham_id = request.POST['LoaiKham']
    # bn.BSPhuTrach = request.POST['BSPhuTrach']
    # bn.PhongKham_id = request.POST['PhongKham']
    bn.save()
    return redirect('/BenhNhan')
@login_required
def FormAddBN(request):
    bs = BacSi.objects.all()
    lk = LoaiKham.objects.all()
    pk = PhongKham.objects.all()
    context = {'bs':bs, 'lk':lk, 'pk':pk}
    return render(request, 'BenhNhan/AddBN.html', context)
@login_required
def AddBN(request):
    bn = BenhNhan.objects.create(
        BenhNhan_id = request.POST['ID'],
        Name = request.POST['Name'],
        Age = request.POST['Age'],
        Gender = request.POST['Gender'],
        LoaiKham_id = LoaiKham.objects.get(LoaiKham_id = request.POST['LoaiKham']),
        BSPhuTrach = BacSi.objects.get(BacSi_id = request.POST['BSPhuTrach']),
        PhongKham_id = PhongKham.objects.get(PhongKham_id = request.POST['PhongKham']),
    )
    bn.save()
    return redirect("/BenhNhan")
@login_required
def DelBN(request, id):
    bn = BenhNhan.objects.get(BenhNhan_id = id)
    bn.delete()
    return redirect("/BenhNhan")
def Fillter(request):
    bn = BenhNhan.objects.filter(LoaiKham_id = request.POST['LoaiKham'], BSPhuTrach = request.POST['BSPhuTrach'], Name__contains = request.POST['Search'])
    lk = LoaiKham.objects.all()
    bs = BacSi.objects.all()
    context = {'bn':bn, 'lk': lk, 'bs' : bs}
    return render(request, 'BenhNhan/ViewBenhNhan.html', context)