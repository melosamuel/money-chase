from django.shortcuts import render
from user_auth.scripts.validators import RegisterForm

def login(request):
    if request.method == "GET":
        return render(request, 'user_auth/login.html')

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            return None
        
        return render(request, 'user_auth/register.html', {'form': form})

    return render(request, 'user_auth/register.html', {'form': form})

def reset_password(request):
    if request.method == "GET":
        return render(request, 'user_auth/reset_password.html')
