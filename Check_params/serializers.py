from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields='__all__'

class DeveloperSerializer(serializers.ModelSerializer):
  class Meta:
    model=Developer
    fields='__all__'

  
