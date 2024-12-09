from django import forms
from .models import User, Student, Teacher, Admin

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','user_type','mobile', 'password')

    def save(self, commit=True):
        if self.cleaned_data['user_type'] == 'admin':
            user = super().save(commit=False)
            user.is_staff = True
            user.user_type = 'admin'


        elif self.cleaned_data['user_type'] == 'teacher':
            user = super().save(commit=False)
            user.user_type = 'teacher'
        else:
            user = super().save(commit=False)
        
            user.user_type = 'student'
        

        if commit:
            user.save()
            if(user.user_type=='admin'):
                Admin.objects.create(user=user)
            if(user.user_type=='teacher'):
                Teacher.objects.create(user=user)
            elif(user.user_type=='student'):
                Student.objects.create(user=user)
            
            
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))