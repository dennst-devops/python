#-#-#-#-#-#-#-#-#-#-
# TripBuddy2APP3  views.py (4)
#-#-#-#-#-#-#-#-#-#-
#add to TripBuddy2PROJ3/apps/TripBuddy2APP3/views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import Trip
from django.contrib import messages
import bcrypt
import datetime
from time import gmtime, strftime, localtime

def index(request):
    if 'pt_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'TripBuddy2APP3/index.html')

def dashboard(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_userid = User.objects.get(id=request.session['pt_id']).id
    these_trips = Trip.objects.filter(tripmaker=this_userid)
    context = {
        "pt_fname": this_user,
        "pt_trips": these_trips,
    }
    return render(request, 'TripBuddy2APP3/dashboard.html', context)

def new(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    context = {
        "pt_fname": this_user,
    }
    return render(request, 'TripBuddy2APP3/newtrip.html', context)

def viewtripdetails(request, ht_tripid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_trip = Trip.objects.get(id=ht_tripid)
    context = {
        "pt_fname": this_user,
        "pt_trips": this_trip,
    }
    return render(request, 'TripBuddy2APP3/viewtrip.html', context)

def edittrip(request, ht_tripid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_trip = Trip.objects.get(id=ht_tripid)
    context = {
        "pt_fname": this_user,
        "pt_trips": this_trip,
    } 
    return render(request, 'TripBuddy2APP3/edittrip.html', context)

##################################################################
# Landing pages above here
##################################################################
# Process routes below here
##################################################################

def register_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['ht_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    User.objects.create(fname=request.POST['ht_fname'], lname=request.POST['ht_lname'], email=request.POST['ht_email'], password=pw_hash)
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    return redirect('/dashboard')

def createnewtrip_process(request):
    errors = Trip.objects.trip_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/new')
    Trip.objects.create(dest=request.POST['ht_dest'], start=request.POST['ht_start'], end=request.POST['ht_end'], plan=request.POST['ht_plan'], tripmaker=User.objects.get(id=request.session['pt_id']))
    return redirect('/dashboard')

def delete(request, ht_tripid):
    if 'pt_id' not in request.session:
        return redirect('/')
    del_trip = Trip.objects.get(id=ht_tripid)
    if request.session['pt_id'] != del_trip.tripmaker.id:
        return redirect('/dashboard')
    del_trip.delete()
    return redirect('/dashboard')

def edit_process(request, ht_tripid):
    this_trip = Trip.objects.get(id=ht_tripid)
    if request.session['pt_id'] != this_trip.tripmaker.id:
        return redirect('/dashboard')
    errors = Trip.objects.edit_trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/edit/'+str(ht_tripid))
    edit_trip = Trip.objects.get(id=ht_tripid)
    if len(request.POST['ht_dest']) > 0:
        edit_trip.dest = request.POST['ht_dest']
    if len(request.POST['ht_start']) == 10:
        edit_trip.start = request.POST['ht_start']
    if len(request.POST['ht_end']) == 10:
        edit_trip.end = request.POST['ht_end']
    if len(request.POST['ht_plan']) > 0:
        edit_trip.plan = request.POST['ht_plan']
    edit_trip.save()
    return redirect('/dashboard')