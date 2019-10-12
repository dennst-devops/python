from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

# Create your views here.
# -#-#-#-#-#-#-#-#-#-
# apps views.py (4)
# -#-#-#-#-#-#-#-#-#-


def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity']=[]
    context = {
        "dj_gold": request.session['gold'],
        "dj_activity": request.session['activity']
    }
    return render(request, 'NinjaApp/index.html', context)

def process(request):
    activityLine=""
    request.session['lnum']=request.POST.get('html_lnum')
    request.session['hnum']=request.POST.get('html_hnum')
    request.session['location']=request.POST.get('html_loc')
    gold_earned=random.randint(int(request.session['lnum']), int(request.session['hnum']))
    print("Gold earned:", gold_earned)
    request.session['gold']+=gold_earned
    current_time = datetime.datetime.now()
    if gold_earned >= 0:
        activityLine="<span class='green'>"
    else:
        activityLine="<span class='red'>"
    if request.session['location'] == "casino":
        activityLine+="Entered a Casino and "
    if gold_earned < 0 and request.session['location'] == "casino":
        activityLine+="and lost "
    elif gold_earned >= 0 and request.session['location'] == "casino":
        activityLine+="and won "
    else:
        activityLine+="Earned "
    activityLine+=str(abs(gold_earned))
    if request.session['location'] != "casino":
        activityLine+=" from the "
        activityLine+=request.session['location'].capitalize()
    activityLine+=" at "
    activityLine+=str(current_time.strftime("%m/%d/%Y %H:%M:%S"))
    activityLine+="</span>"
    print(activityLine)
    request.session['activity'].insert(0,activityLine)
    print(request.session["activity"])
    # return HttpResponse("this is the process route!")
    return redirect('/') 

def resetgold(request):
    print("*"*20)
    activityLine="<span class='blue'>"
    if int(request.session['gold']) > 0:
        activityLine+="Entered the dojo and donated all of your gold."
    elif int(request.session['gold']) < 0:
        activityLine+="Entered the dojo and begged forgivness for your debts."
    else:
        activityLine+="The dojo manager thanks you for your visit."
    activityLine+="</span>"
    print("after activityLine ", activityLine)
    request.session['activity'].insert(0,activityLine)
    request.session['gold'] = 0
    return redirect('/')
    # return HttpResponse("this is the resetgold route!")

def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/') 
    # return HttpResponse("this is the reset route!")
