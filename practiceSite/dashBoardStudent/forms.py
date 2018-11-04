from django import forms
from django.contrib.auth.models import User
from .models import StudentLogin

class StudentLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		models = StudentLogin
		fields = ('username', 'email')
