from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#-#-#-#-#-#-#-#-#-#-
# LoginAndRegAPP  views.py (4)
#-#-#-#-#-#-#-#-#-#-
#add to LoginAndRegPROJ/apps/LoginAndRegAPP/views.py

def index(request):
    return render(request, 'LoginAndRegAPP/index.html')
    # return HttpResponse("this is the equivalent of @app.route('/')!")

def registration_process(request):
    return HttpResponse("this is the equivalent of registration_process!")

def login_process(request):
    return HttpResponse("this is the equivalent of login_process!")

def success(request):
    return HttpResponse("this is the equivalent of success!")

def clear_process(request):
    return HttpResponse("this is the equivalent of clear_process!")