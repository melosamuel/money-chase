from django.urls import path
from user_auth import views

urlpatterns = [
    path('', views.home, name='home')
]
