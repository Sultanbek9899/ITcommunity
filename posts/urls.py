from django.urls import path
from posts.views import (
    IndexPage,
    UserPostsView, 
    PostCreateView, 
    PostDetailView,
    delete_post,
    PostUpdateView,
    archivate_post,
    unarchive_post,
)
urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("my_posts/", UserPostsView.as_view(), name="my_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("post/details/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("post/delete/<int:pk>/",delete_post, name="delete_post"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="update_post"),
    path("post/archivate/<int:pk>/", archivate_post, name="archivate_post"),
    path("post/unarchive/<int:pk>/", unarchive_post, name="unarchive_post")
]