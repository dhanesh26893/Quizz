from django.core.mail import send_mail
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
# from .models import User,TOTPVerification
from .models import User
from django.contrib.auth import authenticate,login
from .forms import UserRegisterForm
# from unittest import mock  
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
                    print("\n\n*******************GOING TO GENERATE OTP*****************\n\n")
                    print("user:",request.user,"\nuser_id:",request.user.id)
                    print("\n\n*******************GOING TO GENERATE OTP*****************\n\n")

                    base32 = pyotp.random_base32()
                    totp = pyotp.TOTP(base32)
                    otp = totp.now()
                    user = User.objects.get(pk = request.user.pk)
                    user.otp = otp 
                    user.save()
                    print("USER OTP SENT:",user.otp)
                    send_mail('OTP Verification',
                                'OTP for {}:{}'.format(user,otp),
                                settings.EMAIL_HOST_USER,
                                [email],fail_silently=False)
                    messages.success(request,f"Dear {user}.. OTP sent successfully!!! Please check your mail..")        
                else:
                    messages.warning(request,"Already sent an email..!!! Please check and verify..")

                # return render(request,"quizapp/home.html")

                # request.session['email'] = email
                # request.session['username'] = username

                return redirect("home")            
        return render(request, 'user/register.html', {'form': form})

class VerifyOtp(View):

    def get(self,request):
        user = request.user
        print("*"*150)
        print(f"""\nuser_id\t:\t{user.id}\n
                \nuser_name\t:\t{user.username}\n
                \nuser_email\t:\t{user.email}\n
                \nuser_otp\t:\t{user.otp}\n""")
        print("*"*150)
        return redirect('home')
    # def get(self,request):
    #         try:
    #             email = request.user.get('email')
    #             otp = request.user.get('otp')
    #             print("\nemail\t:\t",email,"\notp\t:\t",otp)
    #         except:
    #             return redirect('register')
    #         if otp == "000000":
    #             base32 = pyotp.random_base32()
    #             totp = pyotp.TOTP(base32)
    #             otp = totp.now()
    #             user = User.objects.get(pk = request.user.pk)
    #             user.otp = otp 
    #             user.save()
    #             send_mail('OTP Verification',
    #                         'OTP :{}'.format(otp),
    #                         settings.EMAIL_HOST_USER,
    #                         email,fail_silently=False)
    #             messages.success(request,"OTP sent successfully!!! Please check your mail..")        
    #         else:
    #             messages.warning(request,"Already sent an email..!!! Please check and verify..")

    #         return render(request,"user/verifyotp.html") 

    def post(self,request):
        entered_otp = request.POST.get('otp')
        
        print("\nEntered OTP\t:\t",entered_otp)
        
        id = request.user.pk
        user = request.user
        
        print("*"*150)
        print("user_id\t\t:\t\t",user.id)
        print("user_otp\t\t:\t\t",user.otp)
        print("*"*150)
        
        
        mailed_otp = user.otp
        print("\nMailed OTP\t:\t",mailed_otp)
        
        eOTP = int(entered_otp)
        mOTP = int(mailed_otp)
        
        
        if eOTP == mOTP:
            messages.success(request,"Cheers.. OTP Matched..")
            user.is_verified= True 
            user.save()
            return redirect("home")
        else:
            messages.error(request,"Sorry.. OTP Mismatched..")
            return redirect("home")    



# class VerifyOtp(View):
    
#     def get(self,request):
#         try:
#             email = request.user.get('email')
#             otp = request.user.get('otp')
#         except:
#             return redirect('register')


#         if otp == "000000":
#             base32 = pyotp.random_base32()
#             totp = pyotp.TOTP(base32)
#             otp = totp.now()
#             user = User.objects.get(pk = request.user.pk)
#             user.otp = otp 
#             user.save()
#             send_mail('OTP Verification',
#                         'OTP :{}'.format(otp),
#                         settings.EMAIL_HOST_USER,
#                         email,fail_silently=False)
#             messages.success(request,"OTP sent successfully!!! Please check your mail..")        
#         else:
#             messages.warning(request,"Already sent an email..!!! Please check and verify..")
        
#         return render(request,"user/verifyotp.html")

#     def post(self,request):
        
#         try:
#             entered_otp = request.POST.get('otp','0')
#         except:
#             return redirect('register')

#         user = User.objects.get(pk=request.user.pk)
        
#         if int(entered_otp)==int(user.otp):




# from django.views import View
# from django.shortcuts import redirect, render
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from .models import Profile
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.urls import reverse_lazy
# from .forms import UserRegisterForm
# from django.contrib.auth.forms import PasswordChangeForm,AdminPasswordChangeForm
# from django.contrib.auth import update_session_auth_hash

# class homePageView(View):
#     """
#         After successfull login render this template
#     """
#     def get(self,request):
#         # try:
#         #     profile = Profile.objects.get(pk=request.user.pk)
#         # except Profile.DoesNotExist:
#         #     return render(request,"user/home.html")
#         # if profile.is_verified:
#         #     verified = True
#         #     return render(request,"user/home.html",{"verified":verified})
#         # return render(request,"user/home.html")    
#         return redirect('homepage')

# class registerPageView(View):
#     """
#     renders registration page to the User
#     """    
#     def get(self, request):
#         """
#         display the form to the user on get request
#         """
#         form = UserRegisterForm()
#         return render(request, 'user/register.html', {'form': form})

#     def post(self, request):
#         """
#         applying basic validation on the submitted form and saving it to the database
#         """
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             messages.success(request,"Thanks for registering.. You are now logged in..")               

#             email = form.cleaned_data.get("email")
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             new_user = authenticate(username=username,password=password)
#             if new_user:
#                 login(request,new_user)
#                 request.session['email'] = email
#                 request.session['username'] = username
#                 return redirect("homepage")            
#         return render(request, 'user/register.html', {'form': form})


# class verifyProfileOtp(View):
#     def post(self,request):
#         entered_otp = request.POST.get('otp')
#         id = request.user.pk
#         profile = Profile.objects.get(pk=id)
#         mailed_otp = profile.otp
#         eOTP = int(entered_otp)
#         mOTP = int(mailed_otp)
#         if eOTP == mOTP:
#             messages.success(request,"Cheers.. OTP Matched..")
#             profile.is_verified= True 
#             profile.save()
#             return redirect("homepage")
#         else:
#             messages.error(request,"Sorry.. OTP Mismatched..")
#         return redirect("homepage")    


# @method_decorator(login_required(login_url=reverse_lazy("login")),name="dispatch")
# class profilePageView(View):
#     def get(self,request):
#         return render(request,'user/profile.html')


# class ChangeProfilePassword(View):
#     def get(self,request):
        
#         if request.user.is_superuser:
#             form = AdminPasswordChangeForm(request.user)
#             return render(request,"user/changeAdminPassword.html",{"form":form})
#         form = PasswordChangeForm(request.user)
#         return render(request,"user/change_password.html",{"form":form})
    
#     def post(self,request):
#         if request.user.is_superuser:
#             form = AdminPasswordChangeForm(request.user,data = request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 # update_session_auth_hash(request,form.user)
#                 messages.success(request,f"Dear {request.user.username} Your password has been successfully updated!! Please Login again..")
#                 return redirect('login')
#             messages.error(request,f'Dear {request.user.username}, Change Password failed due to Incorrect input.. Please try again..')
#             return redirect('profile')    
        
#         form = PasswordChangeForm(request.user,request.POST)
#         if form.is_valid():
#             user=form.save()
#             messages.success(request,"Your password has been successfully updated!!! Please login..")
#             return redirect('profile')
#         messages.error(request,"Change Password failed due to Incorrect input.. Please try again..")
# return redirect('profile')