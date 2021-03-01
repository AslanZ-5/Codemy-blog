from django import forms
from .models import Post, Category

# cat = [
#     ("cod", "cod"),
#     ("set", "set"),
#     ("mod", "mod")
# ]
## CREATING SAME LIST LIKE ABOVE THROUGH TAKING CATEGORY FROM DB

choices = Category.objects.all().values_list('name', 'name')
choices_list = [i for i in choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'category', 'body','snippet','header_image')  # 'author',
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.TextInput(attrs={"class": "form-control", "placeholder":"user name","value":"","id":"elder"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(choices=choices_list, attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }
