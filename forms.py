from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    user = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()