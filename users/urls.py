from django.urls import path
from . import views as users_views

urlpatterns = [
    path("", users_views.Users.as_view()),
    path("me/", users_views.Me.as_view()),
    path("@<str:username>/", users_views.PublicUser.as_view()),
    path("change-password", users_views.ChangePassword.as_view()),
    path("log-in", users_views.LogIn.as_view()),
    path("log-out", users_views.LogOut.as_view()),
]