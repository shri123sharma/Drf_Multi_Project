from django.contrib import admin
from .models import *
# Register your models here.
class RoleAdmin(admin.ModelAdmin):
  model=Role
  list_display=['role_name']
admin.site.register(Role,RoleAdmin)

class LangauageAdmin(admin.ModelAdmin):
  model=Langauage
  list_display=['langauage_name']
admin.site.register(Langauage,LangauageAdmin)

class DeveloperAdmin(admin.ModelAdmin):
  model=Developer
  list_display=['developer_user']
admin.site.register(Developer,DeveloperAdmin)

class ProjectAdmin(admin.ModelAdmin):
  model=Project
  list_display=['project_name','project_date','project_end_date']
admin.site.register(Project,ProjectAdmin)

class Project_EmployeeAdmin(admin.ModelAdmin):
  model=Project_Employee
  list_display=['project_employee']
admin.site.register(Project_Employee,Project_EmployeeAdmin)





