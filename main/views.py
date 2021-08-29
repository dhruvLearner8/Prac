from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Comp_detail, Desc
import smtplib
import random
import email.message

# Create your views here.
def home(request):
    return render(request,'home.html')

# Create your views here.
