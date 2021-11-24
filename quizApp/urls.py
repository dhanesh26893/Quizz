from django.urls import path 
from . import views

urlpatterns = [ 
    path('',views.homePageView.as_view(),name="home"),
    path('Quiz/',views.QuizView.as_view(),name="quizes"),
]