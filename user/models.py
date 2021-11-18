from django.db import models



class Profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    otp = models.IntegerField(default=123456)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username