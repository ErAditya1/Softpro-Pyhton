from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate,login,logout

from .models import User , Student, Teacher, Admin


from django.contrib import messages
# from .decorators import user_type_required



def home(request):
    return render(request, 'pages/home.html')

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'registration/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'registration/signup.html')
        if User.objects.filter(mobile=mobile).exists():
            messages.error(request, "Mobile number already registered!")
            return render(request, 'registration/signup.html')
        # Create the user
        password_hashed = make_password(password1)
        
        user = User(username=username, email=email, first_name = first_name , last_name = last_name , mobile=mobile, user_type=user_type, password= password_hashed)
        print(user)
        
        if user_type == 'admin':
            user.is_staff = True
            user.user_type = 'admin'


        elif user_type == 'teacher':
            user.user_type = 'teacher'
        else:
            user.user_type = 'student'

        user.save()
        print(user)
        if user:  # If the user was created successfully, create their respective user profile

            if(user.user_type=='admin'):
                Admin.objects.create(user=user)
            if(user.user_type=='teacher'):
                Teacher.objects.create(user=user)
            elif(user.user_type=='student'):
                Student.objects.create(user=user)
            print("User profile created successfully trying to login")

            login(request, user)  # Log the user in

            if user.user_type == 'student':
                return redirect('student_dashboard')
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            if user.user_type == 'teacher':
                return redirect('teacher_dashboard')
        
        else:
            messages.error(request, "User not created!")
            return render(request, 'registration/signup.html')

    return render(request, 'registration/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwor = request.POST.get('password')
       
        
      
        user=authenticate(request,username=username,password=passwor)

        # user = User.objects.get(username=username)
        print("User:", user)
        if user is not None:
            print("Authenticated user")
            res =login(request, user)
            print("login result:", res)
            # Redirect to a success page
            
            
        #     if user.user_type =='student':
        #         return redirect('student_dashboard')
        #     if user.user_type == 'admin':
        #         return redirect('admin_dashboard')
        #     if user.user_type == 'teacher':
        #         return redirect('teacher_dashboard')
        # if user.check_password(passwor):
        #     print("Authenticated user")
        #     res =login(request, user)
        #     print("login result:", res)
        #          # Redirect to a success page
            
            
        #     if user.user_type == 'student':
        #         return redirect('student_dashboard')
        #     if user.user_type == 'admin':
        #         return redirect('admin_dashboard')
        #     if user.user_type == 'teacher':
        #         return redirect('teacher_dashboard')
        

        # user = User.objects.get(username=username)
      
        # if user.check_password(password):
        #     print("Authenticated user")
            
        #     login(request, user)
           
                
        #     # Redirect to a success page
            
        #     if user.user_type == 'student':
        #         return redirect('student_dashboard')
        #     if user.user_type == 'admin':
        #         return redirect('admin_dashboard')
        #     if user.user_type == 'teacher':
        #         return redirect('teacher_dashboard')
        
        

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'registration/login.html')

def logout_user(request):

    if request.method == 'POST':
        signout(request)
        return redirect('home')  # Redirect to the home page or another page




#@user_type_required('student')
def student_dashboard(request):
    print("username:",request.user.username)
    
    return render(request, 'pages/student/home.html')




#@user_type_required('student')
def profile(request):
    
    user = request.user  
    return render(request, 'pages/student/profile.html', {'user': user})
    # if user:
    #     return render(request, 'pages/student/profile.html', {'user': user})
    # else:
    #     return redirect('login')  # Redirect to the home page or another page


def update_profile(request):

    return render(request, 'pages/student/update_profile.html')


#@user_type_required('student')
def study_material(request):
    return render(request, 'pages/student/study_material.html')

#@user_type_required('student')
def doubt_session(request):
    return render(request, 'pages/student/doubts_session.html')

#@user_type_required('student')
def register_complaint(request):
    return render(request, 'pages/student/register_complaint.html')

#@user_type_required('student')
def feedbacks(request):
    return render(request, 'pages/student/feedbacks.html')

#@user_type_required('student')
def assesments(request):
    return render(request, 'pages/student/assignments.html')

#@user_type_required('student')
def lectures(request):
    return render(request, 'pages/student/lectures.html')


# Teachers dash views

# @user_type_required('teacher')
def teacher_dashboard(request):
    
    return render(request, 'pages/teacher/home.html')






    # Admin Dashboard

#@user_type_required('admin')
def admin_dashboard(request):
    
    return render(request, 'pages/admin/home.html')

#@user_type_required('admin')
def manage_user(request):
    users = User.objects.all()
    return render(request, 'pages/admin/manage_user.html', {'users': users})

#@user_type_required('admin')
def edit_user(request,id):
    u = User.objects.get_object_or_404(pk=id)
    return render(request, 'pages/admin/edit_user.html', {'user': u})

#@user_type_required('admin')
def manage_student(request):
    st = Student.objects.all()
    return render(request, 'pages/admin/manage_student.html',{'students': st})

#@user_type_required('admin')
def manage_teacher(request):
    te = Teacher.objects.all()
    return render(request, 'pages/admin/manage_teacher.html', {'teachers': te})

#@user_type_required('admin')
def manage_admin(request):
    ad = Admin.objects.all()
    return render(request, 'pages/admin/manage_admin.html', {'admins': ad})


def upload_studymaterial(request):

    return render(request, 'pages/admin/upload_study.html')

def upload_lectures(request):
    return render(request, 'pages/admin/upload_lectures.html')

def upload_assesments(request):
    return render(request, 'pages/admin/upload_assesments.html')

def view_feedback(request):
    return render(request, 'pages/admin/view_feedback.html')

def view_complaint(request):
    return render(request, 'pages/admin/view_complaint.html')

def view_enquries(request):
    return render(request, 'pages/admin/view_enquries.html')


def add_notification(request):
    return render(request, 'pages/admin/add_notification.html')
