from django.shortcuts import render,redirect

from.models import user

def home(request):
    users = user.objects.all()
    return render(request, 'home.html', {'users': users})



def saveInfo(request):
    name = request.POST['name']
    age = request.POST['age']
    branch = request.POST['branch']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    
    s = user(phone_number, name, age, branch, email )
    s.save()
    # home(request)
    data = user.objects.all()
    return redirect('home')
    
def editInfo(request, phone_number):
    user = user.objects.get(pk=phone_number)
    users = user.objects.all()
    return render(request, 'home.html', {'users': users, 'edit':user})


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
# Create your views here.
