from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index.html')
def index2(request):
    if request.session.has_key('lid'):
        a=request.session['lid']
        return render(request, 'index2.html')
    else:
        return HttpResponseRedirect('login')
def about(request):
    return render(request, 'about.html')