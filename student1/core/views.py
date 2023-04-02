from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.db.models.signals import post_save
import numpy as np
import matplotlib.pyplot as plt

from .models import User, Teachers, Subjects, Student, Standard, Marks, Assignment

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def log_id(request):
    return render(request, 'core/log.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("core:index"))
        else:
            return render(request, "core/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'core/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "core/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "core/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request, "core/index.html", {
            "message": username,
        })
    else:
        return render(request, "core/register.html")
    

def add(request):
        return render(request, "core/attendance.html")
    

def start(request):
    t = Subjects.objects.all()
    return render(request, "core/form.html", {
        "q": t,
    })

def send_end(request):
    t = request.GET.get('title')
    m = request.GET.get('mark')

    q = Marks(subject=t, mark=m)
    q.save()
    return render(request, "core/form.html", {
        "m": "Add Another",
    })

def result(request):
    student = Student.objects.all()
    t = Marks.objects.all()
    total = 0
    for mark in t:
        total = total + mark.mark
    per = (total/600)*100

    grade = 'F'
    if per >= 90.0:
        grade = 'A'
    elif per >= 80.0 and per <= 90.0:
        grade = 'B'
    elif per >= 70.0 and per <= 60.0:
        grade = 'C'


    return render(request, "core/report.html", {
        "sub":t,
        "t":total,
        "per":per,
        "grade": grade,
        "bacha":student,
    })

def navbar(request):
    return render(request, "core/sidebar.html")

def nav(request):
    return render(request, 'core/navbar.html')

def personaal_info(request):
    return render(request, "core/personal.html")

# def timetable(request):
#    return render(request, "core/time-table.html")
def timetable(request):
    return render(request, "core/timetable.html")

def assignment(request):
    name = request.GET.get('name')
    file = request.GET.get('content')

    q = Assignment(name=name, upload=file)

    return render(request, 'core/assignment.html')

def contact(request):
    return render(request, "core/contact.html")

def about(request):
    return render(request, 'core/about.html')


    