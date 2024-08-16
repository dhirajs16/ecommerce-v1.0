from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms  

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']
        labels = {
            'password':'Re-enter Password',
            'email': 'Enter Email'
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'first_name': forms.TextInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'last_name': forms.TextInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'password': forms.PasswordInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'email': forms.EmailInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
        }
        
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Enter Username',
            'password': 'Enter Password',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'password': forms.PasswordInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
        }