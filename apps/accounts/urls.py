from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView
)

urlpatterns = [
    path("signin/", views.SigninView.as_view(), name="signin"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("signout/", LogoutView.as_view(), name="signout"),
    path("profile/",views.profile, name="profile")
]
