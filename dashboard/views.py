from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import History, Meal
from . import flags

import django.contrib.auth as auth
#import RPi.GPIO as GPIO
import datetime
import time
import os

######################################################
#GPIO PIN CONFIGURATION SORTED ASC FROM LEFT TO RIGHT
GPIO_PIN_BCM	= [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]
GPIO_PIN_BOARD	= [4, 17, 18, 27, 22, 23, 24, 25, 5, 6, 12, 13, 19, 16, 26, 20, 21]
######################################################

# Time and Date, to filter meals from today only
yesterday = datetime.date.today() - datetime.timedelta(days=1)

@login_required(login_url='/login')
def index(req) :
	if (req.method == 'POST' and req.POST.get('gpio_pin') and not flags.isRunning) :
		api_rpi_gpio(GPIO_PIN_BOARD[int(req.POST['gpio_pin'])])
		user = User.objects.get(pk=req.POST['user_id'])
		meal = Meal.objects.get(pk=req.POST['meal_id'])
		history = History(user=user, meal=meal)
		history.save()
		return redirect('dashboard/history')

	user = req.user
	diet_history = History.objects.filter(user=user, time__gt=yesterday).all()
	cal_taken = 0
	
	for u in diet_history:
		cal_taken += u.meal.calorie

	cal_left = 400 - cal_taken
	list_of_meal = Meal.objects.filter(calorie__lt=cal_left).order_by('id')[::1]
	context = {'list_of_meal': list_of_meal, 'cal_left': cal_left, 'cal_taken': cal_taken}
	return render(req, 'dashboard/index.html', context)

@login_required(login_url='/login')
def user(req):
	user = req.user
	diet_history = History.objects.filter(user=user, time__gt=yesterday).all()
	cal_taken = 0
	
	for u in diet_history:
		cal_taken += u.meal.calorie

	cal_left = 400 - cal_taken
	context = {'cal_taken': cal_taken, 'cal_left': cal_left}
	return render(req, 'dashboard/user.html', context)
	
@login_required(login_url='/login')
def history(req) :
	user = req.user
	diet_history = History.objects.filter(user=user).order_by('time')[::-1]
	context = {'diet_history': diet_history}
	return render(req, 'dashboard/history.html', context)

def logout(req) :
	auth.logout(req)
	return redirect('/login')

def api_rpi_gpio(pin):
	#If RPi.GPIO is working #################################
	#GPIO.setmode(GPIO.BOARD)
	#Setup pin for dynamo, GPIO5 for LED Green, GPIO6 for LED Red
	#led_green_pin = GPIO_PIN_BOARD[8]
	#led_red_pin = GPIO_PIN_BOARD[9]
	#GPIO.setup(pin, GPIO.OUT)
	#GPIO.setup(led_green_pin, GPIO.OUT)
	#GPIO.setup(led_red_pin, GPIO.OUT)

	#GPIO.output(led_green_pin, GPIO.LOW)
	#GPIO.output(led_red_pin, GPIO.HIGH)
	#GPIO.output(pin, GPIO.HIGH)
	#time.sleep(1)
	#GPIO.output(led_red_pin, GPIO.LOW)
	#GPIO.output(led_green_pin, GPIO.HIGH)
	#GPIO.output(pin, GPIO.LOW)

	#GPIO.cleanup()
	#########################################################
	if (not flags.isRunning) :
		flags.isRunning = True
		os.system("echo '{0}' > /sys/class/gpio/export".format(pin))
		os.system("echo '5' > /sys/class/gpio/export")
		os.system("echo '6' > /sys/class/gpio/export")
		#Setup pin for dynamo, GPIO5 for LED Green, GPIO6 for LED Red
		os.system("echo 'out' > /sys/class/gpio/gpio{0}/direction".format(pin))
		os.system("echo '1' > /sys/class/gpio/gpio{0}/value".format(pin))
		os.system("echo 'out' > /sys/class/gpio/gpio5/direction")
		os.system("echo '0' > /sys/class/gpio/gpio5/value")
		os.system("echo 'out' > /sys/class/gpio/gpio6/direction")
		os.system("echo '1' > /sys/class/gpio/gpio6/value")
		time.sleep(3)
		os.system("echo '0' > /sys/class/gpio/gpio6/value")
		os.system("echo '1' > /sys/class/gpio/gpio5/value")
		os.system("echo '0' > /sys/class/gpio/gpio{0}/value".format(pin))
		os.system("echo 'in' > /sys/class/gpio/gpio{0}/direction".format(pin))
		os.system("echo '{0}' > /sys/class/gpio/unexport".format(pin))
		flags.isRunning = False