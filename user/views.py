from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm,ProfileVerifyForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth import authenticate,login

class homePageView(View):
    """
        After successfull login render this template
    """
    def get(self,request):
        try:
            profile = Profile.objects.get(pk=request.user.pk)
        except Profile.DoesNotExist:
            return render(request,"user/home.html")
        # print("id we get------------>",id)
        # profile.is_verified=True
        # profile.save()
        if profile.is_verified:
            verified = True
            return render(request,"user/home.html",{"verified":verified})
        return render(request,"user/home.html")    
    # template_name = "user/home.html"


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

            # request.session['data'] = form.cleaned_data
                return redirect("home")
            
            
            # return redirect('login')
        return render(request, 'user/register.html', {'form': form})


class verifyProfileOtp(View):
    def post(self,request):
        entered_otp = request.POST.get('otp')
        print("entered otp:",entered_otp)
        id = request.user.pk
        profile = Profile.objects.get(pk=id)
        mailed_otp = profile.otp
        print("otp sent:---->",mailed_otp)
        # print(type(entered_otp))
        # print(type(mailed_otp))
        eOTP = int(entered_otp)
        mOTP = int(mailed_otp)
        if eOTP == mOTP:
            messages.success(request,"OTP Matched..")
            print("\nOTP Matched\n")
            profile.is_verified= True 
            profile.save()
            return redirect("home")
        else:
            messages.error(request,"OTP Mismatched")
            print("\n\nOTP Mismatched\n\n")
        return redirect("home")    


class profilePageView(View):
    def get(self,request):
        id = request.user.pk
        profile = Profile.objects.get(pk=id)


        print("id:",id)
        if request.user.is_authenticated:
                print("user authenticated")
        else:
                print("no authenticated")
        print(request.user.id)
        # profile = Profile.objects.get(pk=id)
        # print(profile)
        form = ProfileVerifyForm()

        return render(request,'user/profile.html',{"form":form})




# def generate_otp():
#     otp = ""
#     for i in range(6):
#         otp+=str(random.randint(0,9))
#     return otp

# @receiver(post_save, sender=User)
# def check_otp(sender, instance,created, **kwargs):
#     if created:
#         username = instance.username
#         email = instance.email

#         otp = generate_otp()

#         subject = "OTP Verification"
#         message = f"Hello {username}. OTP for verification is - {otp}"
#         email_from = settings.EMAIL_HOST_USER
#         recipient = [email]
#         print("\n\nsubject:",subject)
#         print("message:",message)
#         print("email from:",email_from)
#         print("recepient:",recipient,"\n\n")
#         send_mail(subject,message,email_from,recipient,fail_silently=False)

#         return redirect("home")
    
    # instance.profile.save()

