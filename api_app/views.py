from django.shortcuts import render
from django.http import HttpResponse
from api_app import scrap

# Create your views here.
def home(request):
    return HttpResponse("Hi there")

def country_info(request, cname):
    print(cname)
    url = 'https://en.wikipedia.org/wiki/' + cname
    print(url)
    scrap.startSrapping(url)

    return HttpResponse('wait')
    