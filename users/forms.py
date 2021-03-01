from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from datetime import datetime, date
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    data_of_birth = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "data_of_birth", "phone_number", "password1",
                  "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = "form-control"
        self.fields["password1"].widget.attrs['class'] = "form-control"
        self.fields["password1"].widget.attrs['class'] = "form-control"


class ProfileChangeForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-check"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_superuser']


class PasswordChangeManuallyForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","type":"password"}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","type":"password"}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","type":"password"}))

    class Meta:
        model = User
        fields = ["old_password", ]
