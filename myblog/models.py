from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def save(self,*args,**kwargs):
        self.name = self.name.lower()
        return super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myblog:home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, default="detail blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    likes = models.ManyToManyField(User,related_name="blog_post")
    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse('myblog:post_detail', args={str(self.pk)})
