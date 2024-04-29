from django.urls import path
from . import views as users_views

urlpatterns = [
    path("me/", users_views.Me.as_view()),
]