from django.urls import path
from .views import HomeView,PostDetail,AddPost,DeletePost,UpdatePost

app_name = "myblog"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('add-post/',AddPost.as_view(),name='add_post'),
    path('update-post/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    path('delete-post/<int:pk>/',DeletePost.as_view(),name='delete_post'),
]