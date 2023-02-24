from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
  role_name=models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
    return self.role_name

class Langauage(models.Model):
  langauage_name=models.CharField(max_length=255,null=True,blank=True)
  
  def __str__(self):
    return self.langauage_name

class Developer(models.Model):
  developer_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='user_developer')
  developer_roler=models.ForeignKey(Role,null=True,blank=True,on_delete=models.CASCADE,related_name='role_developer')
  developer_langauage=models.ManyToManyField(Langauage,related_name='langauage_developer',blank=True)

  def __str__(self):
    return self.developer_user.username

class Project(models.Model):
  project_user=models.ForeignKey(User,null=True,blank=True,related_name='user_project',on_delete=models.CASCADE)
  project_langauage=models.ManyToManyField(Langauage,related_name='langauage_project',blank=True)
  project_name=models.CharField(max_length=255,null=True,blank=True)
  project_date=models.DateField(null=True,blank=True)
  project_end_date=models.DateField(null=True,blank=True)

  def __str__(self):
    return self.project_name

class Project_Employee(models.Model):
  project_employee=models.ForeignKey(Project,null=True,blank=True,related_name='employee_project',on_delete=models.CASCADE)
  project_employee_developer=models.ManyToManyField(Developer,related_name='employee_developer',blank=True)
  
