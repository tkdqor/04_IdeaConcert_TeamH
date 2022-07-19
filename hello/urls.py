from django.urls import path

from hello.views import GetHello, RedirectHello

app_name = "hello"

urlpatterns = [
    path("", RedirectHello.as_view(), name="redirect_hello"),
    path("api/hello", GetHello.as_view(), name="hello"),
]
