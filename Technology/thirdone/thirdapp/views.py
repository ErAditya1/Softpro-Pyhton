from django.shortcuts import render

def Home(request):
    var = "hihihihi"
    return render(request, 'home.html', {'var': var})

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

# Create your views here.
