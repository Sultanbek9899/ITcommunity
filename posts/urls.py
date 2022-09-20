from django.urls import path
from posts.views import IndexPage

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
]