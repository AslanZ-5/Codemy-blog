from django.shortcuts import render
from django.views.generic import (ListView,
                                  DeleteView,
                                  CreateView,
                                  )
from django.urls import reverse_lazy

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'


class PostDetail(DeleteView):
    model = Post
    template_name = 'myblog/list_detail.html'


class AddPost(CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'myblog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePost(DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('myblog:home')

