from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username','email','password']

    def __str__(self):
        return self.username
