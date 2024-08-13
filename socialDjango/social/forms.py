from django import forms
from .models import Social
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class SocialForm(forms.ModelForm):
    class Meta:
        model=Social
        fields=['text', 'image']


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')