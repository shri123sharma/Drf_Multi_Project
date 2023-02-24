from django.shortcuts import render
from .serializers import *
from .views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import  Q
# Create your views here.
class UserView(APIView):
  permission_classes=(permissions.IsAuthenticated,)
  def get(self, request, *args, **kwargs):
    user_data=User.objects.filter(id=request.user.id)
    user_serializer=UserSerializer(user_data,many=True)
    return Response(user_serializer.data)

  def post(self, request, *args, **kwargs):
    user_serializer=UserSerializer(data=request.data)
    if user_serializer.is_valid():
      user_serializer.save()
      return Response(user_serializer.data,status=status.HTTP_201_CREATED)

class DeveloperView(APIView):
  permission_classes=(permissions.IsAuthenticated,)
  def get(self, request, *args, **kwargs):
    # import pdb;pdb.set_trace()
    developer = Developer.objects.all()
    if self.request.query_params:

      developer_email = self.request.query_params.get("developer_email")
      developer_name = self.request.query_params.get("developer_name")
      developer_role = self.request.query_params.get("developer_role")

      developer=Developer.objects.filter(Q(developer_role=developer_role) |Q(developer_email=developer_email) | Q(developer_name__username=developer_name))
    developer_serializer=DeveloperSerializer(developer,many=True)
    return Response(developer_serializer.data)

  
  def post(self, request, *args, **kwargs):
    import pdb;pdb.set_trace()
    developer_serializer=UserSerializer(data=request.data)
    if developer_serializer.is_valid():
      developer_serializer.save()
      if self.request.query_params:
        developer_role=self.request.query_params['developer_role']
        if developer_role:
            developer_role_filter=Developer.objects.filter(developer_role=developer_role)
            developer_filter_serializer=DeveloperSerializer(developer_role_filter,many=True)
            return Response(developer_filter_serializer.data)  

        developer_email=self.request.query_params['developer_email']
        if developer_email:
          developer_email_filter=Developer.objects.filter(developer_email=developer_email)
          developer_filter_serializer=DeveloperSerializer(developer_email_filter,many=True)
          return Response(developer_filter_serializer.data) 

        developer_name=self.request.query_params['developer_name']
        if developer_name:
          developer_name_filter=Developer.objects.filter(developer_name=developer_email)
          developer_filter_serializer=DeveloperSerializer(developer_name_filter,many=True)
          return Response(developer_filter_serializer.data) 

      return Response(developer_serializer.data,status=status.HTTP_201_CREATED)





