import email
from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from .models import Contact


# Create your views here.

def index(request):
    if request.method == "POST":
        contact=Contact()

        Fname=request.POST.get('Fname')
        Lname=request.POST.get('Lname')
        Email=request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Message = request.POST.get('Message')

        contact.Fname=Fname
        contact.Lname=Lname
        contact.Email=Email
        contact.Phone=Phone
        contact.Msg=Message
        contact.save()

        messages.success(request, "Message sent successfully")
        return render(request,'index.html')
    else:
        return render(request, 'index.html')
