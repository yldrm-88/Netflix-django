from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import login, authenticate,logout
from .models import *

def userLogin(request):
    if request.method == "POST":
        username = request.POST["userName"]
        userpass = request.POST["userPass"]
        user = authenticate(username=username, password=userpass)
        if user is not None:
            login(request, user)
            return redirect('browse')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def profiles(request):
    profiller = Profiles.objects.filter(user=request.user)
    context = {
        'profiller': profiller
    }
    return render(request, 'browse.html', context)

def register(request):
    form = UserForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "register.html", context)
    return render(request, 'register.html', context)

def createProfile(request):
    form = ProfileForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            return redirect("browse")
        else:
            return render(request, "create-profile.html", context)
    return render(request, "create-profile.html", context)


def userLogout(request):
    logout(request)
    return redirect('index')


def userAccount(request):
    account=request.user
    context={
        'account':account
    }
    return render(request,"hesap.html",context)



def deleteAccount(request):
    user=request.user
    user.delete()
    return redirect('index')