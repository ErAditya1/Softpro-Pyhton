from django.shortcuts import render , HttpResponse

def home(request):
    # return HttpResponse("Hello, World!")
    name = 'Aditya Kumar'
    return render(request, 'home.html',{'Name':name})




5

def about(request):
    return render(request, 'about.html')

# Create your views here.
