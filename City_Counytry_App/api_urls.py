from django.urls import path,include
from City_Counytry_App import views
from .views import *

urlpatterns=[
    path('city_api/',CityView.as_view(),name='city_api')
]