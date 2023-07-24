from django.shortcuts import render, HttpResponse
from .models import uc

# Create your views here.


def home(req):
    data = list(uc.find())
   
    return render(req, 'home.html', {"data": data})
    

def about(req):
    return render(req, 'about.html')


def service(req):
    return render(req, 'service.html')


def testinomical(req):
    return render(req, 'testinomical.html')


def contact(req):
    return render(req,'contact.html')