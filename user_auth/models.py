from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birthday = models.TimeField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)