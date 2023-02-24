from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 

# normal View
def sendSimpleEmail(request):
  subject = 'This_Food_Detail_Offer_Type_Post'
  message = f'Hi,thank you for registering in.'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ["sshrikant919@gmail.com"]
  context={
    'subject':subject,
    'message':message,
    'email_from':email_from,
    'recipient_list':recipient_list
  }
  htmly = get_template('email.html')
  html_content = htmly.render(context)
  send_mail( subject, message, email_from, recipient_list,html_message=html_content)
  return HttpResponse('send_mail')

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            context={
              'subject':subject,
              'message':message,
              'email_from':from_email,
              }
            htmly = get_template('email.html')
            html_content = htmly.render(context)
            try:
                send_mail(subject, message,  "sshrikant919@gmail.com",[from_email],html_message=html_content)
                # return HttpResponse('send_mail')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
    return render(request, "new_email.html", {"form": form})





