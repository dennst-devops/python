from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import PostMessage
from .models import Comment
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
    #return redirect('/success')
    return redirect('/wall')

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    #print(key) #just to get rid of the annoying underline above...
    # return redirect('/success')
    return redirect('/wall')

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

def wall(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    context = {
        "pt_fname": this_user,
        "all_messages": PostMessage.objects.all(),
        "all_comments": Comment.objects.all(),
    }
    return render(request, 'LoginAndRegAPP/wall.html', context)

def post_message(request):
    print("#"*30)
    print(request.POST['ht_messagetxt'])
    errors = PostMessage.objects.message_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    PostMessage.objects.create(postmessage=request.POST['ht_messagetxt'], messagemaker=User.objects.get(id=request.session['pt_id']))
    return redirect('/wall')

def post_comment(request):
    print("#"*30)
    print(request.POST['ht_commenttxt'])
    errors = Comment.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    print("$"*30)
    Comment.objects.create(comment=request.POST['ht_commenttxt'], commentmaker=User.objects.get(id=request.session['pt_id']), commenttomessage=PostMessage.objects.get(id=request.POST['ht_msgid']))
    return redirect('/wall')
#del msg
#del cmt
