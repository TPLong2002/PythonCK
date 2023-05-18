from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def FormLogin(request):
    return render(request, "Login/Login.html")
def Login(request):
    username = request.POST["Username"]
    password = request.POST["Password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/Login/Home')
    else:
        return render('Fail')
def Logout(request):
    logout(request)
    return redirect('/Login')
def Home(request):
    return render(request, "Login/LoginSuccess.html")
