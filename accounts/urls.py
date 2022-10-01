from django.urls import path

from accounts.views import  (
    LoginView, 
    logout_user, 
    UserRegisteView,
    UpdateUserView,
    UsersSearchListView
    
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", UserRegisteView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
    path("search/", UsersSearchListView.as_view(), name="user_search")
]