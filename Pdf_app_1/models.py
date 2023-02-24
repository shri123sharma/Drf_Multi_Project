from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=100,null=True,blank=True)
  age=models.PositiveIntegerField()
  email=models.EmailField(max_length=100,null=True,blank=True)
  address=models.CharField(max_length=100,null=True,blank=True)
  phone = PhoneField(blank=True, help_text='Contact phone number')
  country=models.CharField(max_length=100,null=True,blank=True)
  state = models.CharField(max_length=100,default="OH")
  city=models.CharField(max_length=100,null=True,blank=True)
  zip_code = models.CharField(max_length=8, default="43701")
  profile_created_date=models.DateField(auto_now_add=True)
  profile_updated_date=models.DateField(auto_now=True)
  
