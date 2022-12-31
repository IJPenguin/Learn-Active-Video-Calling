from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def base_page_route(request: HttpRequest) -> HttpResponse:
    """[Function]"""

    return render(request, "room/index.html")


def class_page_route(request: HttpRequest) -> HttpResponse:
    """[Function]"""

    return render(request, "room/class.html")
