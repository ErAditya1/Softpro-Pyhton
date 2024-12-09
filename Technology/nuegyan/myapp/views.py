from django.shortcuts import render, redirect
from .models import userinfo, enquiry
def home(request):
    return render(request, 'home.html')

# Create your views here.
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def layout(request):
    return render(request, 'layout.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html' )

def showdata(request):
    show = userinfo.objects.all()
    e = enquiry.objects.all()
    return render(request, 'showdata.html',{'users':show, 'enquirys':e})

def save(request):
    # get data from form
    id = request.POST['id']
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    message = request.POST['message']
    s = userinfo(id=id, name=name, email=email, mobile=mobile, message=message)
    
    s.save()
    return redirect('showdata')

def edit(request,id):
    a = userinfo.objects.get(pk=id)
    return render(request, 'register.html',{'user':a})

def update(request, id):
    a = userinfo.objects.get(pk=id)
    a.name = request.POST['name']
    a.email = request.POST['email']
    a.mobile = request.POST['mobile']
    a.message = request.POST['message']
    a.save()
    return redirect('showdata')

def delete(request,id):
    a = userinfo.objects.get(pk=id)
    a.delete()
    return redirect('showdata')