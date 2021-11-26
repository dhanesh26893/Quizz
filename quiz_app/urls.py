from django.urls import path 
from . import views

urlpatterns = [ 
    path('',views.HomePageView.as_view(),name="home"),
    # path('Quiz/',views.QuizView.as_view(),name="quizes"),
    path('take_quiz/',views.TakeQuiz.as_view(),name="take_quiz"),
]