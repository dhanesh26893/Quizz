from django.shortcuts import render
from .models import (Quiz,Questions,Answer,Quiz_Taken)
from user.models import User
from django.views import View
import pyotp


class homePageView(View):
    
    """
        After successfull login render this template
    """
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            if user.is_verified==True:
                Quizes = Quiz.objects.all()
                return render(request,"quizapp/home.html",{"verified":True,"Quizes":Quizes})
            Quizes = Quiz.objects.all()        
            return render(request,"quizapp/home.html",{"verified":False,"Quizes":Quizes})
        return render(request,"quizapp/home.html")    
class QuizView(View):
    def get(self,request):
        if request.user.is_authenticated():
            Quizes = Quiz.objects.all()
            return render(request,"quizapp/home.html",{"Quizes":Quizes})
        return render(request,"quizapp/home.html")