from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
import os

@login_required(login_url='/login')
def index(req) :
	return render(req, 'dashboard/index.html', None)

@login_required(login_url='/login')
def user(req) :
	return render(req, 'dashboard/user.html', None)
	
@login_required(login_url='/login')
def history(req) :
	return render(req, 'dashboard/history.html', None)

def logout(req) :
	auth.logout(req)
	return redirect('/login')