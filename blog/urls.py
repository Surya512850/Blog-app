from django.urls import path,include
from .views import HomeView,ArticleView,AddPost,UpdatePost,DeletePost,UserPosts,previous_posts,PreviousView,previous_update

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleView.as_view(),name='article_details'),
    path('create/',AddPost.as_view(),name = 'create_blog'),
    path('article/edit/<int:pk>',UpdatePost.as_view(),name = 'update_blog'),
    path('article/<int:pk>/delete',DeletePost.as_view(),name = 'delete_blog'),
    path('posts/previous/<int:pk>',previous_posts,name = "previous-posts"),
    path('posts/<author>',UserPosts.as_view(),name= 'user_posts'),
    path('previous/<int:pk>',PreviousView.as_view(), name = 'previous-details'),
    path('previous/<int:pk>/edit',previous_update, name = 'previous-update')
]
