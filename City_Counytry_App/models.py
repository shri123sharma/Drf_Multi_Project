from django.db import models

# Create your models here.
class Country(models.Model):
  country_name=models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
    return f'{self.country_name}'

class City(models.Model):
  country=models.ForeignKey(Country,blank=True,null=True,on_delete=models.CASCADE,related_name='country_city')
  city_name=models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
    return f'{self.city_name}'
    