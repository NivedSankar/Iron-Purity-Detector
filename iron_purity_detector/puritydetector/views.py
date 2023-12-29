from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def user_input(request):
    return render(request,'user_input.html')