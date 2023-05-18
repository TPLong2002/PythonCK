from django.shortcuts import render, redirect
from.models import PhongKham
from django.contrib.auth.decorators import login_required
@login_required
def viewPhongKham(request):
    pk = PhongKham.objects.all()
    context = {'pk':pk}
    return render(request, 'PhongKham/viewPhongKham.html', context)
@login_required
def DelPhongKham(request, id):
    l = PhongKham.objects.get(PhongKham_id = id)
    l.delete()
    return redirect('/PhongKham')
@login_required
def FormPhongKham(request):
    return render(request, 'PhongKham/FormPhongKham.html')
def AddPhongKham(request):
    l = PhongKham.objects.create(Name = request.POST['Name'])
    l.save()
    return redirect('/PhongKham')
@login_required
def EditPhongKham(request):
    l = PhongKham.objects.get(PhongKham_id = request.POST['ID'])
    l.Name = request.POST['Name']
    l.save()
    return redirect('/PhongKham')
