
def get_user( request):
    user_data = request.session.get('user_data')
    if user_data and user_data.get('is_authenticated'):
        print(user_data)
        return user_data
    return None

def logout(request):
    request.session.clear()
    return redirect('login')

def login(request, user):
    # print(user)
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'mobile': user.mobile,  
        'user_type': user.user_type,  
        'is_authenticated': True,
    }
    request.session.create()
    request.session['user_data'] = user_data
    
