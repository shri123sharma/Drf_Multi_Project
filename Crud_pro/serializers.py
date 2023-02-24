from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class Role_Serializer(serializers.ModelSerializer):
  data =  serializers.SerializerMethodField()
  class Meta:
    model=Role
    fields=['role_name', 'data']
  def get_data(self, obj):
    role_new=''
    if 'http' in obj.role_name:
      for i in obj.role_name.split(' '):
        if 'http' in i:
          a=f'<a href="{i}">{i}</a>'
          role_new+=a+' '
          continue
        role_new+=i+' '
      return role_new
    else:
      return obj.role_name
  


class Langauage_Serializer(serializers.ModelSerializer):
  class Meta:
    model=Langauage
    fields=['langauage_name']

class Developer_Serializer(serializers.ModelSerializer):
  
  class Meta:
    model=Developer
    fields=['developer_user','developer_roler','developer_langauage']
  
  def to_representation(self, instance):
    data=super().to_representation(instance)
    data['developer_user'] = instance.developer_user.username if instance.developer_user else ''
    data['developer_roler'] = instance.developer_roler.role_name if instance.developer_roler else ''
    Repr_list=[]
    for dev_langauage in instance.developer_langauage.all():
      Repr_list.append(dev_langauage.langauage_name)
      data['developer_langauage']=Repr_list
    return data
  
  # def get_developer_user(self,obj):
  #   l=[]
  #   if obj.developer_user:
  #       queryset=Developer.objects.filter(developer_user_id=obj.developer_user.id)
  #       for i in queryset:
  #         if i.developer_user is not None:
  #           l.append(User_Serializer(i.developer_user).data)
  #       return l
  
  # def get_developer_langauage(self,obj):
  #     # import pdb;pdb.set_trace()
  #     return obj.developer_langauage.all().values_list('langauage_name',flat=True)
      
  # def get_developer_roler(self,obj):
  #   l=[]
  #   if obj.developer_roler:
  #     queryset=Developer.objects.filter(developer_roler=obj.developer_roler.id)
  #     for i in queryset:
  #       if i.developer_roler is not None:
  #         l.append(Role_Serializer(i.developer_roler).data)
      # return l

class Project_Employee_Serializer(serializers.ModelSerializer):
  project_developer=serializers.SerializerMethodField()

  class Meta:
    model=Project_Employee
    fields=['project_developer']

  def get_project_developer(self,obj):
    pro_dev_list=[]
    for pro_emp_dev in obj.project_employee_developer.all():
      pro_dev_list.append(Developer_Serializer(pro_emp_dev).data)   
    return pro_dev_list

class Project_Serializer(serializers.ModelSerializer): 
  project_lang = serializers.SerializerMethodField()
  project_employee=serializers.SerializerMethodField(read_only=False)
  
  class Meta:
    model=Project
    fields=['project_user','project_lang','project_name','project_date','project_end_date','project_employee',]

  def to_representation(self, instance):
    data =  super().to_representation(instance)
    data['project_user'] = instance.project_user.username if instance.project_user else ''
    return data

  
  def get_project_lang(self,obj):
    # import pdb;pdb.set_trace()
    l=[]
    for data in obj.project_langauage.all().values_list('langauage_name',flat=True):
      l.append(data)
    return l

  def get_project_employee(self,obj):
      for emp_pro in obj.employee_project.all():
        object=Project_Employee_Serializer(emp_pro).data
        for key,value in object.items():
          del (key)
          return value

class TestSerializer(serializers.ModelSerializer):
  project_role = serializers.SerializerMethodField()

  class Meta:
    model = Project_Employee
    fields=('project_role','project_employee')

  def to_representation(self, instance):
    data =  super().to_representation(instance)
    data['project_employee'] = Project.objects.filter(id=instance.project_employee_id).first().project_name
    return data
  
  def get_project_role(self,obj):
    import pdb;pdb.set_trace()
    user_id = self.context['user_id']
    return obj.project_employee_developer.all().filter(developer_user=user_id).first().developer_roler.role_name

class User_Serializer(serializers.ModelSerializer):
  user_language=serializers.SerializerMethodField()
  project_hired_by_user=serializers.SerializerMethodField()
  project_name_by_user=serializers.SerializerMethodField()
  project_worked=serializers.SerializerMethodField()

  class Meta:
    model=User
    fields=['username','user_language','project_hired_by_user','project_name_by_user','project_worked']

  def get_user_language(self,obj):
    user_langauage=[]
    for dev_user_langauage in obj.user_developer.all():
      for dev_user_langauage_1 in dev_user_langauage.developer_langauage.all():
        user_langauage.append(dev_user_langauage_1.langauage_name)
      return user_langauage

  def get_project_hired_by_user(self,obj):
    return obj.user_project.all().count()
  
  def get_project_name_by_user(self,obj):
    pro_list=[]
    Pro_user=obj.user_project.all()
    for Pro_name in Pro_user:
      pro_list.append(Pro_name.project_name)
    return pro_list

  def get_project_worked(self,obj):
    # import pdb;pdb.set_trace()
    pro_user_project=Project_Employee.objects.filter(project_employee_developer__developer_user=obj.id)
    return TestSerializer(pro_user_project, context= {'user_id':obj.id}, many=True).data

