from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.db import IntegrityError
from django import forms
import cv2
from pyzbar import pyzbar
import numpy as np
from django.utils import timezone
import time

attendance=[]

@login_required(login_url="/login")
def index(request):
    if request.user.is_teacher:
        return render(request, 'qr/fac.html')
    else:
        return render(request, 'qr/student_index.html')

#Faculty Important Details to update their Profile
@login_required(login_url="/login")
def fac_details(request):
    user=User.objects.get(username=request.user.username)
    name_list=[i.first_name for i in Faculty.objects.all()]
    uniq_list=[i.Unique_id for i in Faculty.objects.all()]
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        uniq=request.POST['unique_id']
        sub=request.POST['sub']
        if fname in name_list:
            return render(request,'qr/fac_details.html' ,{
                'msg':"Name exists"
            })
        elif uniq in uniq_list:
            print("ho raha hai kya")
            return render(request, 'qr/fac_details.html',{
                'msg':"Check your unique_id"
            })
        else:
            fac=Faculty.objects.create(first_name=fname, last_name=lname,Subject=sub,Unique_id=uniq,user=user)
            fac.save()
            return HttpResponseRedirect(reverse('index'))
        #create model to save more details
    else:
        return render(request, "qr/fac_details.html")


#Now these is the step towards the scanning attendance and mark it.
@login_required(login_url="/login")
def mark_attendance(request):
    video= cv2.VideoCapture(0)
    user=User.objects.get(username=request.user.username)
    faculty=Faculty.objects.get(user=user)
    subject=faculty.Subject

    while True:
        _, frame= video.read()
        objectDecode= pyzbar.decode(frame)
        for content in objectDecode:
            data=content.data.decode("utf-8")
            for i in MarkAttendance.objects.all():
                attendance.append(i.Mis_no)
                print(attendance)
            if data not in attendance:
                student=Student.objects.get(Mis_no=data)
                name=student.name
                dept=student.Dept
                roll=student.Roll_no
                mark=MarkAttendance.objects.create(name=name,Mis_no=data, roll_no=roll, subject=subject, Department=dept, datetime=timezone.now(), user=user)
                mark.save()
                time.sleep(5)
            else:
                msg="this Qrcode had been scanned before"
                print("This is the same qrcode scanned before")
        cv2.imshow("Scanner",frame)
        key=cv2.waitKey(10) & 0xFF
        if key==27:
            cv2.destroyAllWindows()
            break

    return render(request,'qr/fac.html')

@login_required(login_url="/login")
def get_details(request):
    user=User.objects.get(username=request.user.username)
    name_list=[i.name for i in Student.objects.all()]
    Mis_list=[i.Mis_no for i in Student.objects.all()]
    if request.method == "POST":
        name=request.POST['name']
        roll=request.POST['Roll_no']
        dept=request.POST['Depth']
        mis=request.POST['mis_no']
        sem=request.POST['Semester']
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
            student=Student.objects.create(name=name,Roll_no=roll, Dept=dept,Mis_no=mis,sem=sem,user=user)
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

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
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
            user = User.objects.create_user(username=username, email=email, password=password, is_teacher=is_teacher)
            user.save()
            login(request, user)
            if not user.is_teacher:
                return HttpResponseRedirect(reverse("get_details"))
            else:
                return HttpResponseRedirect(reverse("fac_details"))
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "qr/register.html", {
                "message": "Username already taken."
                })
    else:
        return render(request, "qr/register.html")
