from django.http import HttpResponse
from django.shortcuts import redirect
from .models import UrlEntry


def index(request):
    '''Generates simple content for default page'''
    return HttpResponse('This is URL shortening service. Please provide id of the URL, e.g. http://localhost:8000/A7dw')


def redirect_url(request, short_id):
    '''Transforms short url into a long one and then redirects user to it'''
    result = UrlEntry.objects.filter(short_id=short_id)
    if not result:
        return HttpResponse(f'URL with id "{short_id}" was not found')
    return redirect(result[0].value)
