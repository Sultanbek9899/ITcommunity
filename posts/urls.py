from django.urls import path
from posts.views import IndexPage, UserPostsView, PostCreateView

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("my_posts/", UserPostsView.as_view(), name="my_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post")
]