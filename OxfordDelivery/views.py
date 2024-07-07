from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You are now tuned to the best delivery services ever")


def home_page(request):
    return render(request, 'OxfordDelivery/home.html')