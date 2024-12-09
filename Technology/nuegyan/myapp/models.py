from django.db import models




# Create your models here.

class userinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=15)
    message = models.CharField(max_length=500)   

class enquiry(models.Model):
    phone = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=125)
    email = models.EmailField(max_length=100)
    message = models.TextField( max_length=500)


   