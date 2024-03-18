from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages


def home_view(request):
    return render(request,'homepage.html')


def login_user(request):
    pass

def logout_user(request):
    pass