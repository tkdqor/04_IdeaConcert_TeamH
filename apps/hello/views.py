from django.http import HttpResponse


def hello(request):
    content = "Hello"
    return HttpResponse(content)
