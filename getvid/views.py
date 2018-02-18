from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Show statistics by Provider, Category.")
    return render(request, "getvid/index.html",{})
    
def udemy(request):
    return HttpResponse("Show all UDEMY pending & completed courses.")
    
def lynda(request):
    return HttpResponse("Show all LYNDA pending & completed courses.")