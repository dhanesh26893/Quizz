from django.urls import path
from django.contrib.auth import views as authViews
from .views import VerifyOtp, registerPageView
    

urlpatterns = [

    path('register/', registerPageView.as_view(), name="register"),
    path('login/', authViews.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', authViews.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path('otpVerification/', VerifyOtp.as_view(), name="otp_verification"),
]