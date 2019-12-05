from django import forms
from django.contrib.auth.models import User
from .models import Profile, Team
from django.contrib.auth.forms import UserCreationForm
from colleges import *
from django.db import models

class UserForm(UserCreationForm):
	email = forms.EmailField(max_length=255, label="E-Mail")
	college = forms.ChoiceField(choices=colleges_list, label="College")
	gender = forms.ChoiceField(choices=[('', "Choose your gender"),('F', 'Female'),('M', 'Male'),("O", "Others"),("X", "Prefer not to say")], label="Gender")
	first_name = forms.CharField(max_length=255, label="First Name")
	last_name = forms.CharField(max_length=255, label="Last Name")
	class Meta:
		model=User
		# fields = '__all__'
		fields = ('first_name', 'last_name', 'gender', 'college', 'username', 'email')

# class ProfileForm(forms.ModelForm):
# 	user_college = forms.ChoiceField(choices=colleges_list, label="College")
# 	user_state = forms.CharField(max_length=50, label="State/UT") # TODO: change this to choices

# 	class Meta:
# 		model = Profile
# 		fields = ('user_college', 'user_state')

class CreateTeamForm(forms.ModelForm):
	team_name = forms.CharField(max_length=20, label="Team Name")
	class Meta:
		model=Team
		fields = ['team_name']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(required=False, widget=forms.FileInput)
	class Meta:
		model=Profile
		fields = ['bio','image']