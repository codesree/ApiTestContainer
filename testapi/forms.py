from django import forms
from .models import Userpro
from django.contrib.auth.models import User

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')



