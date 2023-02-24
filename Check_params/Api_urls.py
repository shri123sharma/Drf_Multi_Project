from django.urls import path,include
from Check_params import views
from .views import *

urlpatterns=[
      path('user_api/',UserView.as_view(),name='user'),
      path('developer_api/',DeveloperView.as_view(),name='developer')
]