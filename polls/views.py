from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return render(request, 'base.html')

def second(request):
    return HttpResponse("World")

def third(request):
    return HttpResponse("Rohit")