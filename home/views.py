from django.shortcuts import render
from django.urls import *
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    aboutUs=AboutUs.objects.all()
    return render(request,'about.html',{"aboutUs":aboutUs})

def contact(request):
    contact=Contact.objects.all()
    return render(request,'contact.html',{"contact":contact})
