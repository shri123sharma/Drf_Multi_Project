from django.shortcuts import render
from City_Counytry_App import views
from .views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import permissions
from .serializers  import *
# Create your views here.
class CityView(APIView):
  permission_classes=(permissions.IsAuthenticated,)
  def get(self, request, *args, **kwargs):
    city_data=City.objects.all()
    context={}
    if self.request.query_params:
      city_id = self.request.query_params.get("city_id")
      context['city_id']=city_id
    city_serializer=CitySerializer(city_data,many=True, context=context)
    return Response(city_serializer.data)


