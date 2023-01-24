from django.urls import path,include
from .import views
from .views import GeneratePdf

app_name="Pdf_app_1"
urlpatterns = [
  # path('userpdf/<int:id>/',views.user_pdf,name='user-pdf-generate'),
  path('generatepdf/<int:id>/',GeneratePdf.as_view(),name='generatepdf'),
]
