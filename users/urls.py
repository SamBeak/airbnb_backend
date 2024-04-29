from django.urls import path
from . import views as users_views

urlpatterns = [
    path("", users_views.Users.as_view()),
    path("me/", users_views.Me.as_view()),
]