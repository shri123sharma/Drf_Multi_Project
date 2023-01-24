from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import User
from django.shortcuts import reverse,redirect
from django.views import View
from django.http import HttpResponseRedirect
import datetime

# def user_pdf(request,id,*args,**kwargs):
#   # import pdb;pdb.set_trace()
#   pdf_=io.BytesIO()
#   data=canvas.Canvas(pdf_)
#   data.drawString(200,200,"this is pdf generate")
#   data.showPage()
#   data.save()
#   pdf_.seek(0)
#   return FileResponse(pdf_,as_attachment=True,filename="user_pdf.pdf")

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 

class GeneratePdf(View):
    def get(self, request,id, *args, **kwargs):
        # import pdb;pdb.set_trace()
        context={}
        context['user']=User.objects.filter(id=id).first()
        pdf = render_to_pdf('admin/Pdf_app_1/demo.html', context)
        return HttpResponse(pdf, content_type='application/pdf')





