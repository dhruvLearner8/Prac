from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.
def home(request):
    return render(request,'home.html')

# Create your views here.
