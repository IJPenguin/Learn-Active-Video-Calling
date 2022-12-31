from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def signin_page_route(request: HttpRequest) -> HttpResponse:
    """[Function]"""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
        return redirect("/")
    return render(request, "core/signin.html")


def signup_page_route(request: HttpRequest) -> HttpResponse:
    """[Function]"""

    if request.method == "POST":
        username = request.POST.get("username")
        if username is None:
            return redirect(reverse("sigup"))
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
        except Exception as exception:
            pass
        else:
            login(request, user=user)
        return redirect("/")
    return render(request, "core/signup.html")


def signout_page_route(request: HttpRequest) -> HttpResponse:
    """[Function]"""

    logout(request)
    return redirect("/")
