from django import forms
# from django.contrib.auth.models import User
from dashBoardStudent.models import UserLogin

class UserForm(forms.ModelForm):
    # password = forms.CharField(widget = forms.PasswordInput)
    class Meta():
        model = UserLogin
        fields = ('username', 'password')
