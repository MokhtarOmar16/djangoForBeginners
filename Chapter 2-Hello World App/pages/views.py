from django.shortcuts import render
from django.http import HttpResponse


# the data will be shown in urls    
# Create your views here.
def HomePage(req):
    return HttpResponse("hello world")