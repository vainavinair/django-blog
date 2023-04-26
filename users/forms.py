from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm): #inherits django UserCreationForm
    email= forms.EmailField() #required is true by default
    first_name= forms.TextInput()
    last_name= forms.TextInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']