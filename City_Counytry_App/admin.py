from django.contrib import admin
from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
  model=Country
  list_display=['id','country_name']
admin.site.register(Country,CountryAdmin)

class CityAdmin(admin.ModelAdmin):
  model=City
  list_display=['id','city_name']
admin.site.register(City,CityAdmin)

