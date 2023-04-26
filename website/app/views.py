"""importing render"""
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def store(request):
    """creating a function named as home"""
    return render(request, "base.html")


def profile(request):
    """creating a function named as home"""
    return render(request, "home.html")


def signup(request):
    """creating a function named as home"""
    if request.method == "POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        Password_confirmation = request.POST.get("Password_confirmation:")
        obj = User.objects.create(username=fname, email=email, phone=phone)
        obj.save()
    return render(request, "signup.html")


def index(request):
    """creating a function named as home"""
    return render(request, "index.html")


def products(request):
    """creating a function named as home"""
    return render(request, "products.html")
