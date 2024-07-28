from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at my homepage")
    return render(request, "website/index.html")

def about(request):
    return HttpResponse("Hello, world. You are at my about us page")

def contact(request):
    return HttpResponse("Hello, world. You are at my contact us page")