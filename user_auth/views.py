from django.shortcuts import render
from user_auth.scripts.get_countries import get_world_places

def login(request):
    return render(request, 'user_auth/login.html')

def register(request):
    places = get_world_places()

    return render(request, 'user_auth/register.html', {'places': places})

def reset_password(request):
    return render(request, 'user_auth/reset_password.html')
