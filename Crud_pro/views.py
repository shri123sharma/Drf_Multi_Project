from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.db import connection
from rest_framework.serializers import *


# Create your views here.
class User_View(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_data = User.objects.filter(id=request.user.id).first()
        if user_data:
            user_serializer = User_Serializer(user_data)
            return Response(user_serializer.data)

    def post(self, request, pk, *args):
        user_serializer = User_Serializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_404_Bad_Request)


class Role_View(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        role_data = Role.objects.all()
        role_serializer = Role_Serializer(role_data, many=True)
        return Response(role_serializer.data)

    def post(self, request, *args):
        role_serializer = Role_Serializer(data=request.data)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response(role_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(role_serializer.errors, status=status.HTTP_404_Bad_Request)

    def put(self, request, pk, *args, **kwargs):
        role_data = Role.objects.get(pk=pk)
        role_serializer = Role_Serializer(
            role_data,
            data=request.data,
        )
        if role_serializer.is_valid():
            role_serializer.save()
            return Response(role_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(role_serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(
        self,
        request,
        pk,
    ):
        try:
            role_data = Role.objects.get(pk=pk)
            role_data.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT,
            )
        except Role.DoesNotExist:
            return HttpResponse("this objects does not exist")


class Language_View(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        langauage_data = Langauage.objects.all()
        langauage_serializer = Langauage_Serializer(langauage_data, many=True)
        return Response(langauage_serializer.data)

    def post(self, request, *args):
        langauage_serializer = Langauage_Serializer(data=request.data)
        if langauage_serializer.is_valid():
            langauage_serializer.save()
            return Response(langauage_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                langauage_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk, *args):
        langauage_data = Langauage.objects.get(pk=pk)
        langauage_serializer = Langauage_Serializer(langauage_data, data=request.data)
        if langauage_serializer.is_valid():
            langauage_serializer.save()
            return Response(
                langauage_serializer.data, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            return Response(
                langauage_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(
        self,
        request,
        pk,
    ):
        try:
            role_data = Langauage.objects.get(pk=pk)
            role_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Langauage.DoesNotExist:
            return HttpResponse("this objects does not exist")


class Developer_View(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args):
        developer_data = Developer.objects.all()
        developer_serializer = Developer_Serializer(developer_data, many=True)
        return Response(developer_serializer.data)

    def post(self, request, *args):
        developer_serializer = Developer_Serializer(data=request.data)
        if developer_serializer.is_valid():
            developer_serializer.save()
            return Response(developer_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                developer_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk, *args):
        developer_data = Developer.objects.filter(pk=pk).first()
        developer_serializer = Developer_Serializer(developer_data, data=request.data)
        if developer_serializer.is_valid():
            developer_serializer.save()
            return Response(
                developer_serializer.data, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            return Response(
                developer_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(
        self,
        request,
        pk,
    ):
        try:
            role_data = Developer.objects.get(pk=pk)
            role_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Developer.DoesNotExist:
            return HttpResponse("this objects does not exist")


class Project_View(APIView):
    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
    ):
        # import pdb;pdb.set_trace()
        project_data = Project.objects.all()
        project_serializer = Project_Serializer(project_data, many=True)
        return Response(project_serializer.data)

    def post(self, request, *args):
        project_serializer = Project_Serializer(data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                project_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk, *args):
        project_data = Project.objects.get(pk=pk)
        project_serializer = Project_Serializer(project_data, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(
                project_serializer.data, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            return Response(
                project_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(
        self,
        request,
        pk,
    ):
        try:
            role_data = Project.objects.get(pk=pk)
            role_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return HttpResponse("this objects does not exist")


class Project_Employee_View(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Project_Serializer

    def get(self, request):
        project_employee_data = Project_Employee.objects.all()
        project_employee_serializer = Project_Employee_Serializer(
            project_employee_data, many=True
        )
        return Response(project_employee_serializer.data)

    def post(
        self,
        request,
    ):
        project_employee_serializer = Project_Employee_Serializer(data=request.data)
        if project_employee_serializer.is_valid():
            project_employee_serializer.save()
            return Response(
                project_employee_serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                project_employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        project_employee_data = Project_Employee.objects.get(pk=pk)
        project_employee_serializer = Project_Employee_Serializer(
            project_employee_data, data=request.data
        )
        if project_employee_serializer.is_valid():
            project_employee_serializer.save()
            return Response(
                project_employee_serializer.data, status=status.HTTP_205_RESET_CONTENT
            )
        else:
            return Response(
                project_employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(
        self,
        request,
        pk,
    ):
        try:
            role_data = Project_Employee.objects.get(pk=pk)
            role_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project_Employee.DoesNotExist:
            return Response("this objects does not exist")
