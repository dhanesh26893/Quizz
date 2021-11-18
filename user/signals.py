from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    range_start = 10**5
    range_stop = (10**6)-1
    return random.randint(range_start,range_stop)

@receiver(post_save, sender=User)
def createProfile(sender, instance,created, **kwargs):
    if created:
        username = instance.username
        email = instance.email
        # password = instance.password1
        otp = generate_otp()
        print("\n\nusername\t:\t",username)
        print("email\t:\t",email)
        print("otp\t:\t",otp,"\n\n")
        Profile.objects.create(
            username=username,
            email=email,
            otp = otp
            # password = password
        )

        print("profile created")

        subject = "Please Confirm your account"
        message = f'Your 6 Digit Verification Pin: {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [str(email), ]
        mail = send_mail(subject, message, email_from, recipient_list,fail_silently=False)
        if mail:
            print("*"*100)
            print("mail sent successfully")
            print("*"*100)
        else:
            print("*"*100)
            print("mail failed")
            print("*"*100)
    # instance.profile.save()