from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse


# Create your views here.

@login_required
def index(request):
    return render(request, 'qr\index.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"] 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "qr/login.html", {
                "message": "Invalid username and/or password."
                })
    return render(request, "qr/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        is_teacher=False
        if "is_teacher" in request.POST.keys():
            is_teacher = request.POST["is_teacher"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "qr/register.html",  {
                "message": "Passwords must match."
                })
        try:
            user = User.objects.create_user(username=username, email=email, password=password, is_teacher=is_teacher)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "qr/register.html", {
                "message": "Username already taken."
                })
    return render(request, "qr/register.html")