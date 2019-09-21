from django.http import HttpResponse
from django.shortcuts import redirect
from .models import UrlEntry


def index(request):
    return HttpResponse('This is URL shortening service. Please provide id of the URL, e.g. http://localhost:8000/A7dw')


def redirect_url(request, short_id):
    result = UrlEntry.objects.filter(short_id=short_id)
    if not result:
        return HttpResponse(f'URL with id "{short_id}" was not found')
    return redirect(result[0].value)
