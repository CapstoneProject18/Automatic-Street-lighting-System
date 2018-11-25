from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ComplaintForm, LoginForm
from django.contrib.auth import authenticate, login

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
			return redirect("/admin")
		else:
			# Return an 'invalid login' error message.
			print ("Error")
	return render(request, "auth/login.html", context)

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

