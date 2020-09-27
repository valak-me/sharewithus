from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=['username','email','password1','password2']


class Userupdateform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class profileupdateform(forms.ModelForm):
    image= forms.ImageField()

    class Meta:
        model= profile
        fields =['image']
