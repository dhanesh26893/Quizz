from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.forms import PasswordChangeForm,AdminPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class homePageView(View):
    """
        After successfull login render this template
    """
    def get(self,request):
        # try:
        #     profile = Profile.objects.get(pk=request.user.pk)
        # except Profile.DoesNotExist:
        #     return render(request,"user/home.html")
        # if profile.is_verified:
        #     verified = True
        #     return render(request,"user/home.html",{"verified":verified})
        # return render(request,"user/home.html")    
        return redirect('homepage')

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
            new_user = authenticate(username=username,password=password)
            if new_user:
                login(request,new_user)
                request.session['email'] = email
                request.session['username'] = username
                return redirect("homepage")            
        return render(request, 'user/register.html', {'form': form})


class verifyProfileOtp(View):
    def post(self,request):
        entered_otp = request.POST.get('otp')
        id = request.user.pk
        profile = Profile.objects.get(pk=id)
        mailed_otp = profile.otp
        eOTP = int(entered_otp)
        mOTP = int(mailed_otp)
        if eOTP == mOTP:
            messages.success(request,"Cheers.. OTP Matched..")
            profile.is_verified= True 
            profile.save()
            return redirect("homepage")
        else:
            messages.error(request,"Sorry.. OTP Mismatched..")
        return redirect("homepage")    


@method_decorator(login_required(login_url=reverse_lazy("login")),name="dispatch")
class profilePageView(View):
    def get(self,request):
        return render(request,'user/profile.html')


class ChangeProfilePassword(View):
    def get(self,request):
        
        if request.user.is_superuser:
            form = AdminPasswordChangeForm(request.user)
            return render(request,"user/changeAdminPassword.html",{"form":form})
        form = PasswordChangeForm(request.user)
        return render(request,"user/change_password.html",{"form":form})
    
    def post(self,request):
        if request.user.is_superuser:
            form = AdminPasswordChangeForm(request.user,data = request.POST)
            if form.is_valid():
                user = form.save()
                # update_session_auth_hash(request,form.user)
                messages.success(request,f"Dear {request.user.username} Your password has been successfully updated!! Please Login again..")
                return redirect('login')
            messages.error(request,f'Dear {request.user.username}, Change Password failed due to Incorrect input.. Please try again..')
            return redirect('profile')    
        
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Your password has been successfully updated!!! Please login..")
            return redirect('profile')
        messages.error(request,"Change Password failed due to Incorrect input.. Please try again..")
        return redirect('profile')
            