import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_old(request):
    html_ = """<!DOCTYPE html>
    <html lang=en>

    <head></head>
    <body>
    <h1>Hello World!</h1>
    <p>This is html coming through</p>
    </body>
    </html>
    """

    return HttpResponse(html_)

def home(request):

    context =  {

    }
    return render(request,"home.html",context)

def home1(request):

    context =  {

    }
    return render(request,"home1.html",context)

def home2 (request):

    context =  {

    }
    return render(request,"home2.html",context)