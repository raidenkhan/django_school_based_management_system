from django.shortcuts import render, redirect
from .models import Master
from .models import Teacher
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def setSession(request):
    role = ""
    if request.POST["role"] == "1":
        role = "Admin"
    if request.POST["role"] == "2":
        role = "Teacher"
    if request.POST["role"] == "3":
        role = "Student"
    request.session["role"] = role


# ADMIN INDEX
def admin_index(request):
    admins = Master.objects.all()
    setSession(request)

    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pass"]
        user = admins.filter(username=username).values()
        print(user)

        if len(user) > 0:
            return render(request, "Master/index.html")
        else:
            error = "Invalid Logins"
            messages.error(request, error)
            return HttpResponseRedirect(
                "/login",
            )
    else:
        error = "Please login first"
        messages.error(request, error)
        return HttpResponseRedirect("/login")


# TEACHERS
def teachers(request):
    print("\n\n\n")
    teachers = Teacher.objects.all().values()

    return render(request, "Master/teacher.html", {"teachers": list(teachers)})


def teacher_add(request):
    return render(request, "Master/teacher-add.html")
