from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import views
from .models import Ram
from .forms import frm
    

# Create your views here.
def index(request):
    return render(request,"register.html")
def createpst(request):
    
    name = request.POST.get("Name")
    password= request.POST.get("Password")
    email= request.POST.get("Email_ID")
    gen= request.POST.get("Gender")
    dob= request.POST.get("Date_of_Birth")
    address= request.POST.get("Address")
    phone= request.POST.get("Phone_Number")
    photo=request.POST.get("Photo")
    a=Ram(Name=name,Password=password,Email_ID= email,Gender=gen,Date_of_Birth=dob,Address=address,Phone_Number=phone,Photo=photo)
    a.save()
    return render(request,"login.html")
