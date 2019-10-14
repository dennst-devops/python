from django.shortcuts import render

# Create your views here.
#-#-#-#-#-#-#-#-#-#-
# apps views.py (4)
#-#-#-#-#-#-#-#-#-#-

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def addnew(request):
    return HttpResponse("this is the equivalent of addnew!")

def allshows(request):
    return HttpResponse("this is the equivalent of allshows!")

def editshows(request):
    return HttpResponse("this is the equivalent of editshows!")

def showdetails(request):
    return HttpResponse("this is the equivalent of showdetails!")

def destroy(request):
    return HttpResponse("this is the equivalent of destroy!")