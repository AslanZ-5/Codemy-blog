from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegistrationForm, ProfileChangeForms, UserProfileChangeForm, PasswordChangeManuallyForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from django.shortcuts import get_object_or_404


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# def ProfileView(request):
#
#     return render(request, 'registration/profile_update.html')


class ProfileShow(generic.DetailView):
    model = Profile
    template_name = "registration/profile_show.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileShow, self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        user = get_object_or_404(User, id=self.kwargs['pk'])
        context["user_profile"] = user_profile
        context['user'] = user
        return context






class ProfileUpdateView(generic.UpdateView):
    form_class = UserProfileChangeForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('myblog:home')

    def get_object(self):
        return self.request.user


class Password_Manualy_ChangeView(PasswordChangeView):
    form_class = PasswordChangeManuallyForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')
