
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    
    # Fixing the clashes with related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Change related_name here
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Change related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username




class Student(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,  related_name='student' )
    Rollno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.CharField( max_length=4)
    Fname = models.CharField(max_length=50)
    Mname = models.CharField(max_length=50)
    Gender = models.CharField(max_length=6)
    Address = models.CharField(max_length=255)
    Program = models.CharField(max_length=50)
    Branch = models.CharField(max_length=50)
    Year = models.CharField( max_length=50)
    Contactno = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='students')
    isVerified = models.BooleanField(default= False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='teacher')
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='admin')
    employee_id = models.CharField(max_length=20)
    office = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


   