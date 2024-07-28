from django.shortcuts import render

# Create your views here.
def allChai(request):
    return render(request, 'myapp/all_chai.html')

