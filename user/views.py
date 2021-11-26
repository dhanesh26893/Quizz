from django.core.mail import send_mail
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate,login
from .forms import UserRegisterForm
import pyotp
from django.conf import settings

class registerPageView(View):
    """
    renders registration page to the User
    """    
    def get(self, request):
        """
        display the form to the user on get request
        """
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        """
        applying basic validation on the submitted form and saving it to the database
        """
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request,"Thanks for registering.. You are now logged in..")               

            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            otp = form.cleaned_data.get('otp')
             
            new_user = authenticate(username=username,password=password)
            if new_user:
                login(request,new_user)
                if not otp:
                    base32 = pyotp.random_base32()
                    totp = pyotp.TOTP(base32)
                    otp = totp.now()
                    user = User.objects.get(pk = request.user.pk)
                    user.otp = otp 
                    user.save()
                    send_mail('OTP Verification',
                                'OTP for {}:{}'.format(user,otp),
                                settings.EMAIL_HOST_USER,
                                [email],fail_silently=False)
                    messages.success(request,f"Dear {user}.. OTP sent successfully!!! Please check your mail..")        
                else:
                    messages.warning(request,"Already sent an email..!!! Please check and verify..")
                return redirect("home")            
        return render(request, 'user/register.html', {'form': form})

class VerifyOtp(View):

    def get(self,request):
        user = request.user
        return redirect('home')

    def post(self,request):
        entered_otp = request.POST.get('otp')
        mailed_otp = request.user.otp
        entered_otp = int(entered_otp)
        mailed_otp = int(mailed_otp)
                
        if entered_otp == mailed_otp:
            messages.success(request,"Cheers.. OTP Matched..")
            request.user.is_verified= True 
            request.user.save()
            return redirect("home")
        else:
            messages.error(request,"Sorry.. OTP Mismatched..")
            return redirect("home")    



