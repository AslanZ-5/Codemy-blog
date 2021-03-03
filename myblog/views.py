from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DeleteView,
                                  CreateView,
                                  UpdateView,
                                  DetailView
                                  )
from django.urls import reverse_lazy, reverse
from .forms import PostForm, AddCategoryForm
from django.http import HttpResponseRedirect

from .models import Post, Category


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("myblog:post_detail", args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(request, 'myblog/category_list.html',
                  {'cats': cats.title().replace("-", " "), "category_posts": category_posts})


class PostDetail(DetailView):
    model = Post
    template_name = 'myblog/list_detail.html'

    def get_context_data(self,**kwargs):
        context = super(PostDetail, self).get_context_data( **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = stuff.total_likes()
        cat_menu = Category.objects.all()
        context['cat_menu'] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = AddCategoryForm
    # fields = '__all__'
    template_name = 'myblog/add_category.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

    
class AllCategories(ListView):
    model = Category
    template_name = 'myblog/all_categories.html'


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
