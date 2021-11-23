from django.shortcuts import render
# from .models import (Quiz,Questions)
from django.views import View

class homePageView(View):

    """
        After successfull login render this template
    """
    def get(self,request):
        return render(request,"quizapp/home.html")

