from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Panelist! You're at the votes index.")