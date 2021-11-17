from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import TemplateView


class homePageView(TemplateView):
    """
    After successfull login render this template
    """
    template_name = "user/home.html"


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
            form.save()
            messages.success(request,"Registration Successfull..Please login..")               
            return redirect('login')
        return render(request, 'user/register.html', {'form': form})
