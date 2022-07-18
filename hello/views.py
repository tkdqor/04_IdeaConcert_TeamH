from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class GetHello(APIView):
    def get(self, request):
        return HttpResponse("hello", status=status.HTTP_200_OK)


class RedirectHello(APIView):
    def get(self, request):
        return redirect("hello:hello")
