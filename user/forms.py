from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name")
    email = forms.EmailField()
    smid = forms.CharField(max_length=10, required=True, help_text="Enter your employee number")


    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'smid', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name")
    email = forms.EmailField()
    smid = forms.CharField(max_length=10, required=True, help_text="Enter your employee number")


    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'smid']

class ProfileUpdateForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ['image']