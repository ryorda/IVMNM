from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import History, Meal
import django.contrib.auth as auth
import RPi.GPIO as GPIO
import datetime
import time
import os

@login_required(login_url='/login')
def index(req) :
	if (req.method == 'POST' and req.POST.get('gpio_pin')) :

		######################################################
		#GPIO PIN CONFIGURATION SORTED ASC FROM LEFT TO RIGHT
		GPIO_PIN_BCM	= [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]
		GPIO_PIN_BOARD	= [4, 17, 18, 27, 22, 23, 24, 25, 05, 06, 12, 13, 19, 16, 26, 20, 21]
		######################################################
		api_rpi_gpio(GPIO_PIN_BOARD[int(req.POST['gpio_pin'])])

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

def api_rpi_gpio(pin):
	GPIO.setmode(GPIO.BOARD)
	#Setup pin for dynamo, GPIO5 for LED Green, GPIO6 for LED Red
	led_green_pin = GPIO_PIN_BOARD[8]
	led_red_pin = GPIO_PIN_BOARD[9]
	GPIO.setup(pin, GPIO.OUT)
	GPIO.setup(led_green_pin, GPIO.OUT)
	GPIO.setup(led_red_pin, GPIO.OUT)

	GPIO.output(led_green_pin, GPIO.LOW)
	GPIO.output(led_red_pin, GPIO.HIGH)
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(led_red_pin, GPIO.LOW)
	GPIO.output(led_green_pin, GPIO.HIGH)
	GPIO.output(pin, GPIO.LOW)

	GPIO.cleanup()