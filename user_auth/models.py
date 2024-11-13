from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)