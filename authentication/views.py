from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from  django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
# Create your views here.


def home(request):
    return render(request, 'authentication/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()                     # save user to database
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'account is registered successfully for {first_name}!Login to the account')
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, 'authentication/registration.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            full_name = request.user.get_full_name()
            # messages.success(request, f'{full_name}!you are logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, "username or password is incorrect")
            return redirect('login')    # if login failed return again to login page
    return render(request, 'authentication/login.html')     # if method is GET


def user_logout(request):
    logout(request)
    messages.info(request,'you are logged out')
    return redirect('login')
