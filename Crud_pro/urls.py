from django.urls import path
from Crud_pro import views
from . import views
from .views import *

urlpatterns = [
    path('user/',views.User_View.as_view(),name='user'),
    path('role/', views.Role_View.as_view(),name='role'),
    path('language/',views.Language_View.as_view(),name='language'),
    path('developer/',views.Developer_View.as_view(),name='developer'),
    path('project/',views.Project_View.as_view(),name='project'),
    path('project_employee/',views.Project_Employee_View.as_view(),name='project_employee'),
  
 
]
