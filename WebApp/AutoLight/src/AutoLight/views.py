from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ComplaintForm, LoginForm
from django.contrib.auth import authenticate, login

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
#GPIO.setup(3, GPIO.OUT)
#GPIO.setup(5, GPIO.OUT)
#GPIO.setup(8, GPIO.OUT)
#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)


def home_page(request):
	contact_form = ComplaintForm(request.POST or None)
	context = {
		"form": contact_form
	}
	
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	
	# if request.method == "POST":
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('nearest_location'))
	# 	print(request.POST.get('complaint'))

	return render(request, "homepage.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in")
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(request.user.is_authenticated)
		if user is not None:
			print(request.user.is_authenticated)
			login(request, user)
			# Redirect to a success page
			#context['form'] = LoginForm()
			return redirect("/dashboard")
		else:
			# Return an 'invalid login' error message.
			print ("Error")
	return render(request, "auth/login.html", context)

def dashboard_page(request):
	return render(request, "dashboard.html")
def weather_page(request):
	return render(request, "weather.html")
def lightcontrol_page(request):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	
	if(request.GET.get('mybtn')):
		GPIO.output(3, GPIO.HIGH)
	if(request.GET.get('mybtn_1')):
		GPIO.output(3, GPIO.LOW)
	if(request.GET.get('mybtn_2')):
		GPIO.output(5, GPIO.HIGH)
	if(request.GET.get('mybtn_3')):
		GPIO.output(5, GPIO.LOW)
	if(request.GET.get('mybtn_4')):
		GPIO.output(8, GPIO.HIGH)
	if(request.GET.get('mybtn_5')):
		GPIO.output(8, GPIO.LOW)
	if(request.GET.get('mybtn_6')):
		GPIO.output(11, GPIO.HIGH)
	if(request.GET.get('mybtn_7')):
		GPIO.output(11, GPIO.LOW)
	if(request.GET.get('mybtn_8')):
		GPIO.output(13, GPIO.HIGH)
	if(request.GET.get('mybtn_9')):
		GPIO.output(13, GPIO.LOW)
	return render(request, "lightcontrol.html")

def user_page(request):
	return render(request, "user.html")

def register_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "auth/register.html", context)


# def about_page(request):
# 	return render(request, "homepage.html", {})
# 
# def contact_page(request):
# 	return render(request, "homepage.html", {})

