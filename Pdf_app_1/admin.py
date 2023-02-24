from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
  model=User
  list_display=('name','age','address','phone','country','state','city',
                'zip_code','profile_created_date','profile_updated_date',
                )

  change_form_template="admin/Pdf_app_1/change_form.html"
admin.site.register(User,UserAdmin)