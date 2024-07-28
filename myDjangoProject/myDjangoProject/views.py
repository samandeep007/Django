from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You are at my homepage")

def about(request):
    return HttpResponse("Hello, world. You are at my about us page")

def contact(request):
    return HttpResponse("Hello, world. You are at my contact us page")