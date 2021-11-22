from django.shortcuts import render
from .models import (Quiz,Questions,FIB,MCQ,UserAnswers)
from django.views import View

class QuizView(View):
    def get(self,request):

        all_quizes = Quiz.objects.all()
            
        return render(request,"quizapp/homepage.html",{'all_quiz':all_quizes})


class TakeQuiz(View):
    def get(self,request):
        quiz_id = request.GET.get('quiz_id')
        questions = Questions.objects.filter(quiz=quiz_id)

        quizz_duration = 0
        quiz_marks = 0

        for i in questions:
            quizz_duration+=questions.time
            quiz_marks+=questions.marks

        