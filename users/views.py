from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationForm, UserProfileChangeForm, PasswordChangeManuallyForm
from .models import Profile


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')


# def ProfileView(request):
#
#     return render(request, 'users/profile_update.html')


def loginview(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myblog:home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myblog:home')
    return render(request,'users/logout.html')


class ProfileShow(generic.DetailView):
    model = Profile
    template_name = "users/profile_show.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileShow, self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_profile"] = user_profile
        return context


class ProfileUpdateView(generic.UpdateView):
    form_class = UserProfileChangeForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('myblog:home')

    def get_object(self):
        return self.request.user


class Password_Manualy_ChangeView(PasswordChangeView):
    form_class = PasswordChangeManuallyForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'users/password_success.html')
