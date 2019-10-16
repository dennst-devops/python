from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
#-#-#-#-#-#-#-#-#-#-
# LoginAndRegAPP  views.py (4)
#-#-#-#-#-#-#-#-#-#-
#add to LoginAndRegPROJ/apps/LoginAndRegAPP/views.py

def index(request):
    return render(request, 'LoginAndRegAPP/index.html')
    # return HttpResponse("this is the equivalent of @app.route('/')!")

def registration_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['ht_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    User.objects.create(fname=request.POST['ht_fname'], lname=request.POST['ht_lname'], email=request.POST['ht_email'], password=pw_hash)
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    return redirect('/success')

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    print(key) #just to get rid of the annoying underline above...
    return redirect('/success')
    # return HttpResponse("this is the equivalent of login_process!")

def success(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    context = {
        "pt_fname": this_user,
    }
    return render(request, 'LoginAndRegAPP/success.html', context)

def clear_process(request):
    request.session.clear()
    return redirect('/')
    # return HttpResponse("this is the equivalent of clear_process!")