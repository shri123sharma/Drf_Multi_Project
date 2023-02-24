from django.contrib import admin
from django.urls import path
from Send_Email import views
from .views import *

app_name='Send_Email'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('mail/',views.sendSimpleEmail),
    path("contact/", contactView, name="contact"),
    # path("success/", successView, name="success"),
    
]