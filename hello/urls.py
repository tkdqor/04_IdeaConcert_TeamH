from django.urls import path

from .views import HelloAPIView

app_name = "hello"

urlpatterns = [
    path("hello/", HelloAPIView.as_view()),
]
