from django.http import request
from django.shortcuts import render
from .models import (Quiz,Questions,Answer,QuizTaken)
from user.models import User
from django.views import View
from django.views.generic import TemplateView,ListView


class HomePageView(View):    
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
        return render(request,"user/login.html")    


class TakeQuiz(View):
    def get(self,request):
        quiz_id = request.GET.get("quiz_id")
        print(quiz_id)
        questions = Questions.objects.filter(quiz_id=quiz_id)
        answers = Answer.objects.select_related('question_id').all()
        # questions_asked = []
        # if questions.question_id == answers.question_id:
            # questions_asked.append(questions.question_id)
        # print(questions_asked)
        for i in answers:
            print(i.question_id.question_id)
            print(i.answer_text)
        print(questions)
        return render(request,"quizapp/take_quiz.html",{"Questions":questions})

