from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import Book
from django.contrib import messages
import bcrypt
import datetime
from time import gmtime, strftime, localtime

def index(request):
    if 'pt_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'BeltPrepAPP/index.html')

def dashboard(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_userid = User.objects.get(id=request.session['pt_id']).id
    these_books = Book.objects.filter(bookmaker=this_userid)
    context = {
        "pt_fname": this_user,
        "pt_books": these_books,
    }
    return render(request, 'BeltPrepAPP/dashboard.html', context)

def newbook(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    context = {
        "pt_fname": this_user,
    }
    return render(request, 'BeltPrepAPP/newbook.html', context)

def viewbookdetails(request, ht_bookid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=ht_bookid)
    if request.session['pt_id'] != this_book.bookmaker.id:
        return redirect('/dashboard')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_book = Book.objects.get(id=ht_bookid)
    context = {
        "pt_fname": this_user,
        "pt_books": this_book,
    }
    return render(request, 'BeltPrepAPP/viewbook.html', context)

def editbook(request, ht_bookid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=ht_bookid)
    if request.session['pt_id'] != this_book.bookmaker.id:
        return redirect('/dashboard')
    this_user = User.objects.get(id=request.session['pt_id']).fname
    this_book = Book.objects.get(id=ht_bookid)
    context = {
        "pt_fname": this_user,
        "pt_books": this_book,
    } 
    return render(request, 'BeltPrepAPP/editbook.html', context)


##################################################################
# Render pages above here
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

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['pt_id'] = User.objects.get(email=request.POST['ht_email']).id
    return redirect('/dashboard')

def logout_process(request):
    request.session.clear()
    return redirect('/')

def createnewbook_process(request):
    if 'pt_id' not in request.session:
        return redirect('/')
    errors = Book.objects.book_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/new')
    Book.objects.create(title=request.POST['ht_title'], publishdate=request.POST['ht_pubdate'], desc=request.POST['ht_desc'], bookmaker=User.objects.get(id=request.session['pt_id']))
    return redirect('/dashboard')

def update_process(request, ht_bookid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=ht_bookid)
    if request.session['pt_id'] != this_book.bookmaker.id:
        return redirect('/dashboard')
    errors = Book.objects.edit_book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/edit/'+str(ht_bookid))
    edit_book = Book.objects.get(id=ht_bookid)
    if len(request.POST['ht_title']) > 0:
        edit_book.title = request.POST['ht_title']
    if len(request.POST['ht_pubdate']) == 10:
        edit_book.publishdate = request.POST['ht_pubdate']
    if len(request.POST['ht_desc']) > 0:
        edit_book.desc = request.POST['ht_desc']
    edit_book.save()
    return redirect('/dashboard')

def delete_process(request, ht_bookid):
    if 'pt_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=ht_bookid)
    if request.session['pt_id'] != this_book.bookmaker.id:
        return redirect('/dashboard')
    del_book = Book.objects.get(id=ht_bookid)
    if request.session['pt_id'] != del_book.bookmaker.id:
        return redirect('/dashboard')
    del_book.delete()
    return redirect('/dashboard')

