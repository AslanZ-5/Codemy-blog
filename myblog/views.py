from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DeleteView,
                                  CreateView,
                                  UpdateView
                                  )
from django.urls import reverse_lazy
from .forms import PostForm

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    # ordering = ['-id']
    ordering = ['-post_date']


class PostDetail(DeleteView):
    model = Post
    template_name = 'myblog/list_detail.html'


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/update_post.html'
    success_url = reverse_lazy('myblog:home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('myblog:home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
