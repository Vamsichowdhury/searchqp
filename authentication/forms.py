from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):  # EXTENDING THE OLD FORM WITH NEW FORM
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-sm",
            'placeholder': "Enter email address",
        }))

    first_name = forms.CharField(
        label='', max_length=100,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-sm",
            "placeholder": "Enter First Name",
        }))
    last_name = forms.CharField(
        label='', max_length=100,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-sm",
            "placeholder": "Enter Last Name",
        }))
    username = forms.CharField(
        label='', max_length=100,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-sm",
            "placeholder": "Enter User Name",
        }))

    password1 = forms.CharField(
        label='', max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-sm",
            "placeholder": "Enter Password",
        }))
    password2 = forms.CharField(
        label='', max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-sm",
            "placeholder": "Confirm Password",
        }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



