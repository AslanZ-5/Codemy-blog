from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    data_of_birth = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "data_of_birth","phone_number","password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = "form-control"
        self.fields["password1"].widget.attrs['class'] = "form-control"
        self.fields["password1"].widget.attrs['class'] = "form-control"
