from django.urls import path

from . import views

urlpatterns = [
    path("signin/", views.signin_page_route, name="signin"),
    path("signup/", views.signup_page_route, name="signup"),
    path("signout/", views.signout_page_route, name="signout"),
]
