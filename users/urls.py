from django.urls import path
from .views import UserRegisterView,ProfileUpdateView,Password_Manualy_ChangeView,password_success
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    # path('password/', auth_view.PasswordChangeView.as_view(template_name="registration/change_password.html"),name='change_password'),
    path('password/', Password_Manualy_ChangeView.as_view(template_name="registration/change_password.html"),name='change_password'),
    path('password_success/',password_success, name="password_success")
]

