from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    otp = models.IntegerField(default=000000)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username','email','password']
    # is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


