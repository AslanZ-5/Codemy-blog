from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrationForm,ProfileChangeForms,UserProfileChangeForm
from django.contrib.auth.models import User


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# def ProfileView(request):
#
#     return render(request, 'registration/profile.html')


class ProfileUpdateView(generic.UpdateView):
    form_class = UserProfileChangeForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('myblog:home')

    def get_object(self):
        return self.request.user
