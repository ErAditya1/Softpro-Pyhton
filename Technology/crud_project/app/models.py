from django.db import models


class user(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


# Create your models here.
