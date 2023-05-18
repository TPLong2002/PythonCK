from django.shortcuts import render, redirect
from .models import LoaiKham
from django.contrib.auth.decorators import login_required
@login_required
def viewLoaiKham(request):
    lk = LoaiKham.objects.all()
    context = {'lk':lk}
    return render(request, 'LoaiKham/viewLoaiKham.html', context)
@login_required
def DelLoaiKham(request, id):
    l = LoaiKham.objects.get(LoaiKham_id = id)
    l.delete()
    return redirect('/LoaiKham')
@login_required
def FormLoaiKham(request):
    return render(request, 'LoaiKham/FormLoaiKham.html')
@login_required
def AddLoaiKham(request):
    l = LoaiKham.objects.create(Name = request.POST['Name'])
    l.save()
    return redirect('/LoaiKham')
@login_required
def EditLoaiKham(request):
    l = LoaiKham.objects.get(LoaiKham_id = request.POST['ID'])
    l.Name = request.POST['Name']
    l.save()
    return redirect('/LoaiKham')
