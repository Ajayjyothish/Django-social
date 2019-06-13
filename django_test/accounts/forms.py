from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpUser(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={ 'type' : 'email', 'placeholder' : 'Email'
        
    }))
	# password2= forms.CharField()
	
	


class Meta:
	model = User
	fields = ("username", "email", "password1")
