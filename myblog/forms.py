from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body')
        widget = {
            "title": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'this is place holder'}),
            "tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Select(attrs={"class": "form-control"})
        }
