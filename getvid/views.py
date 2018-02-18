from django.shortcuts import render
from django.http import HttpResponse
from .models import Provider
from .models import Course

# Create your views here.

def index(request):
    #return HttpResponse("Show statistics by Provider, Category.")
    providersData = Provider.objects.values()
    coursesData = Course.objects.values()
    return render(request, 'getvid/index.html', {'providersData': providersData, 'coursesData': coursesData})
    #return render(request, "getvid/index.html",{})

def udemy(request):
    return HttpResponse("Show all UDEMY pending & completed courses.")

def lynda(request):
    return HttpResponse("Show all LYNDA pending & completed courses.")
