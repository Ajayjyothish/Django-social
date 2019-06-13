from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpUser


# Create your views here.

def accounts_view(request, *args, **kwargs):
	form = SignUpUser()

	if request.method == 'POST':
		form = SignUpUser(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')

	return render(request, 'signup.html', {'form': form})
