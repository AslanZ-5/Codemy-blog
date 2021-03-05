from django.urls import path
from .views import HomeView,PostDetail,AddPost,DeletePost,UpdatePost,AddCategory,CategoryView,AllCategories,likeView,AddComment


app_name = "myblog"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('add-post/',AddPost.as_view(),name='add_post'),
    path('add-category/',AddCategory.as_view(),name='add_category'),
    path('category/<str:cats>/',CategoryView,name='category_list'),
    path('update-post/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    path('delete-post/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('all-categories/',AllCategories.as_view(),name='all_categories'),
    path('like/<int:pk>/', likeView, name="add_like"),
    path('post/<int:pk>/add-comment/',AddComment.as_view(),name="add_comment"),
]