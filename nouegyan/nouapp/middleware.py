from django.shortcuts import redirect

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Define your user type requirements here
        protected_urls = {
            
            'student': '/student/',
            'teacher': '/teacher/',
            'admin': '/admin_u/',

        }
        
        
        print(request.user.is_authenticated)

        for user_type, url_prefix in protected_urls.items():
            if request.path.startswith(url_prefix):
                if not request.user.is_authenticated or request.user.profile.user_type != user_type:
                    return redirect('home')  # Redirect to home or an error page
        return None



# from django.shortcuts import redirect
# from .utils import get_user

# class UserTypeMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         # Define your user type requirements here
#         protected_urls = {
#             'student': '/student_dashboard/',
#             'teacher': '/teacher_dashboard/',
#             'admin': '/admin_dashboard/',
#         }
#         public_urls = ['/login/', '/signup/']
#         user = get_user(request)
#         current_path = request.path

#         for user_type, url_prefix in protected_urls.items():
#             if user :
#                 if  and request.path.startswith(url_prefix) and user.get('is_authenticated'):
#                     # print(user_type)

#                     print (current_path)
#                     print("Current path: " + current_path)
                    


#                     if user.get('user_type') != user_type :
#                         print("I am in condition 2")
#                         if user.get('user_type') == 'student':
#                             return redirect('student_dashboard')
#                         if user.get('user_type') == 'admin':
#                             return redirect('admin_dashboard')
#                         if user.get('user_type') == 'teacher':
#                             return redirect('teacher_dashboard')

#                 elif current_path in public_urls and user.get('is_authenticated'):
#                     print("I am in else condition ")
#                     if user.get('user_type') == 'student':
#                         return redirect('student_dashboard')
#                     if user.get('user_type') == 'admin':
#                         return redirect('admin_dashboard')
#                     if user.get('user_type') == 'teacher':
#                         return redirect('teacher_dashboard')
               

                    
#         return None
