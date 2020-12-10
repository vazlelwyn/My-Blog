from django.urls import path
from .views import HomeView, BlogsView, AddBlogView, UpdateBlogView, DeleteBlogView, likeview

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('Blogs/<int:pk>', BlogsView.as_view(), name="blogs"),
    path('Add_Blog', AddBlogView.as_view(), name="add_blog"),
    path('Blogs/Edit/<int:pk>', UpdateBlogView.as_view(), name="update_blog"),
    path('Blogs/<int:pk>/Delete', DeleteBlogView.as_view(), name="delete_blog"),
    path('Like/<int:pk>', likeview, name='like_blogpost'),
    #path('Blogs/<int:pk>/Comment/', BlogCommentView.as_view(), name="add_comment"),
]
