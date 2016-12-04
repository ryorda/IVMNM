from django.shortcuts import render
from django.http import HttpResponse
import os

def index(req) :
	return render(req, 'dashboard/index.html', None)

def user(req) :
	return render(req, 'dashboard/user.html', None)
	
def history(req) :
	return render(req, 'dashboard/history.html', None)