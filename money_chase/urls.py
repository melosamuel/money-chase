from django.urls import path
from user_auth import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password')
]
