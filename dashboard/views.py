from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import History, Meal
import django.contrib.auth as auth
import datetime
import os

@login_required(login_url='/login')
def index(req) :
	if (req.method == 'POST') :
		user = User.objects.get(pk=req.POST['user_id'])
		meal = Meal.objects.get(pk=req.POST['meal_id'])
		history = History(user=user, meal=meal)
		history.save()
		return redirect('dashboard/history')
		
	list_of_meal = Meal.objects.order_by('id')[::1]
	context = {'list_of_meal': list_of_meal}
	return render(req, 'dashboard/index.html', context)

@login_required(login_url='/login')
def user(req) :
	return render(req, 'dashboard/user.html', None)
	
@login_required(login_url='/login')
def history(req) :
	diet_history = History.objects.order_by('time')[::-1]
	context = {'diet_history': diet_history}
	return render(req, 'dashboard/history.html', context)

def logout(req) :
	auth.logout(req)
	return redirect('/login')