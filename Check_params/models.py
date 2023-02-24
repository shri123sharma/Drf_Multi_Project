from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Developer(models.Model):
  developer_name=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='user')
  developer_role=models.CharField(max_length=100,null=True,blank=True)
  developer_email=models.CharField(max_length=100,null=True,blank=True)

  def __str__(self):
    return f'{self.developer_name} - {self.developer_role} - {self.developer_email}'
