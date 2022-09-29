from django.urls import path
from posts.views import (
    IndexPage,
    UserPostsView, 
    PostCreateView, 
    get_post_detail,
    delete_post, 
)
urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("my_posts/", UserPostsView.as_view(), name="my_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("post/details/<int:pk>/", get_post_detail, name="post_details"),
    path("post/delete/<int:pk>/", delete_post, name="delete_post"),
]