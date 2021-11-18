from django import views
from django.urls import path
from django.contrib.auth import views as authViews
from .views import profilePageView, registerPageView, homePageView, verifyProfileOtp
    

urlpatterns = [
    path('',homePageView.as_view(),name="home"),
    path('register/', registerPageView.as_view(), name="register"),
    path('login/', authViews.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', authViews.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path('profile/',profilePageView.as_view(),name="profile"),
    path('verifyotp/',verifyProfileOtp.as_view(),name="verifyotp")
]