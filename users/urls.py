from django.urls import path
from .views import (UserRegisterView,
                    ProfileUpdateView,
                    Password_Manualy_ChangeView,
                    password_success,
                    ProfileShow,
                    loginview,
                    logoutview,
                    )
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview, name='logout'),
    path('<int:pk>/profile_show/', ProfileShow.as_view(), name='profile_show'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'),
    # path('password/', auth_view.PasswordChangeView.as_view(template_name="users/change_password.html"),name='change_password'),
    path('password/', Password_Manualy_ChangeView.as_view(template_name="users/change_password.html"),
         name='change_password'),
    path('password_success/', password_success, name="password_success")
]
