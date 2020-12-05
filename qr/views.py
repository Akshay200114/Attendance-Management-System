from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.db import IntegrityError
from qrcode import *


@login_required(login_url="/login")
def index(request):
    if request.user.is_teacher:
        return render(request, 'qr/fac.html')
    else:
        return render(request, 'qr/student_index.html')

@login_required(login_url="/login")
def get_details(request):
    user=User.objects.get(username=request.user.username)
    if request.method == "POST":
        name=request.POST['name']
        roll=request.POST['Roll_no']
        dept=request.POST['dept']
        mis=request.POST['mis_no']
        name_list=[i.name for i in Student.objects.all()]
        Mis_list=[i.Mis_no for i in Student.objects.all()]
        if name in name_list:
            return render(request,'qr/more_details.html' ,{
                'msg':"Name exists"
            })
        elif mis in Mis_list:
            print("ho raha hai kya")
            return render(request, 'qr/more_details.html',{
                'msg':"Check your Mis No"
            })
        else:
            student=Student.objects.create(name=name,Roll_no=roll, Dept=dept,Mis_no=mis,user=user)
            student.save()
            return HttpResponseRedirect(reverse('index'))
        #create model to save more details
    else:
        return render(request, "qr/more_details.html")


@login_required(login_url="/login")
def get_qr(request):
    user=User.objects.get(username=request.user.username)
    return render(request,"qr/get_qr.html", {
        'student': Student.objects.get(user=user)
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"] 
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            print("my name is khan")
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "qr/login.html", {
                "message": "Invalid username and/or password."
                })
    else:
        return render(request, "qr/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        is_teacher = False
        if "is_teacher" in request.POST.keys():
            is_teacher = bool(request.POST["is_teacher"])
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "qr/register.html",  {
                "message": "Passwords must match."
                })
        try:
            user = User.objects.create(username=username, email=email, password=password, is_teacher=is_teacher)
            user.save()
            login(request, user)
            if not user.is_teacher:
                return render(request, "qr/more_details.html")
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "qr/register.html", {
                "message": "Username already taken."
                })
    else:
        return render(request, "qr/register.html")
