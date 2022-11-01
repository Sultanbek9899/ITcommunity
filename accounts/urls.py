from mmap import ACCESS_WRITE
from django.urls import path

from accounts.views import  (
    LoginView, 
    logout_user, 
    UserRegisteView,
    UpdateUserView,
    UsersSearchListView,
    FollowUser,
    UnfollowUser,
    UserProfileView,
    change_password,
    password_reset_request
    
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", UserRegisteView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
    path("search/", UsersSearchListView.as_view(), name="user_search"),
    
    path("follow/<int:user_pk>/",FollowUser.as_view(), name="follow" ),
    path("unfollow/<int:user_pk>/", UnfollowUser.as_view(), name="unfollow"),
    path("user/profile/detail/<int:pk>/", UserProfileView.as_view(), name="user_profile_detail"),
    
    path("user/password/change/", change_password, name="change_password"),

    #user password reset paths

    path("password_reset/done/", 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
        name="password_reset_done"),
    
    path("reset/<uidb64>/<token>/", 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path("reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
        name="password_reset_complete"
    ),

    path("user/password/reset/", password_reset_request, name="password_reset"),

]