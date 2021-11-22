from django.urls import path 
from .import views

urlpatterns = [ 
    path('',views.QuizView.as_view(),name="homepage"),
    path('takeQuiz/',views.TakeQuiz.as_view(),name="take_quiz"),
]