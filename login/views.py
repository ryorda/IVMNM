from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(req) :

	if (req.user.is_authenticated) :
		return redirect(req.GET.get('next','/dashboard/'))
		
	if (req.method == 'POST' ) :
		
		username 	= req.POST['username']
		password 	= req.POST['password']
		user 		= authenticate(username=username, password=password)

		if user is not None:
			login(req, user)
			return redirect('/dashboard')
		else:
			return render(req, 'login/index.html', { 'error' : 'username or password is incorrect, try again.'})

	return render(req, 'login/index.html', None)

	