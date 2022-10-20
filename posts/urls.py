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
    FollowingPostsView,
    like_post,
    unlike_post,
    CommentCreatView
)
urlpatterns = [
    path("", FollowingPostsView.as_view(), name="index"),
    path("my_posts/", UserPostsView.as_view(), name="my_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("post/details/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("post/delete/<int:pk>/",delete_post, name="delete_post"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="update_post"),
    path("post/archivate/<int:pk>/", archivate_post, name="archivate_post"),
    path("post/unarchive/<int:pk>/", unarchive_post, name="unarchive_post"),
    path("post/like/<int:post_pk>/", like_post, name="like_post"),
    path("post/unlike/<int:post_pk>/", unlike_post, name="unlike_post"),

    path("post/comment/create/<int:post_id>/", CommentCreatView.as_view(),name="create_comment")

]