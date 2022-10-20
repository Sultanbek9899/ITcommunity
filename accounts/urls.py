from django.urls import path

from accounts.views import  (
    LoginView, 
    logout_user, 
    UserRegisteView,
    UpdateUserView,
    UsersSearchListView,
    FollowUser,
    UnfollowUser,
    UserProfileView
    
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", UserRegisteView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
    path("search/", UsersSearchListView.as_view(), name="user_search"),
    
    path("follow/<int:user_pk>/",FollowUser.as_view(), name="follow" ),
    path("unfollow/<int:user_pk>/", UnfollowUser.as_view(), name="unfollow"),
    path("user/profile/detail/<int:pk>/", UserProfileView.as_view(), name="user_profile_detail")
]