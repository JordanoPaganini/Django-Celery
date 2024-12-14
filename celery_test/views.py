from django.http import HttpResponse
from .task import task1

def test_view(request):
    task1.delay()
    return HttpResponse('Hello, World!!!')