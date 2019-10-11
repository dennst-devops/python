from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Authors

# Create your views here.
def index(request):
    #return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {
        "dj_books": Book.objects.all(),
    }
    return render(request, 'BooksAuthorsApp/index.html', context) 

def bookid(request, ht_showbook):
    this_book = Book.objects.get(id=ht_showbook)
    these_authors = this_book.books_id.all()
    context = {
        "dj_bookid": this_book,
        "dj_authors": these_authors,
    }
    #return HttpResponse("this is the equivalent of bookid")
    return render(request, 'BooksAuthorsApp/books.html', context) 

def addbook(request):
    Book.objects.create(title=request.POST['ht_title'], desc=request.POST['ht_desc'])
    return redirect ('/')

def addauth(request):
    Authors.objects.create(first_name=request.POST['ht_fname'], last_name=request.POST['ht_lname'], notes=request.POST['ht_notes'])
    return redirect ('/')

def authors(request):
    context = {
        "dj_authors": Authors.objects.all(),
    }
    # return HttpResponse("this is the equivalent of authors!")
    return render(request, 'BooksAuthorsApp/addauthor.html', context) 

def authorsid(request, ht_showauth):
    this_auth = Authors.objects.get(id=ht_showauth)
    these_books = this_auth.books.all()
    context = {
        "dj_authid": this_auth,
        "dj_books": these_books,
    }
    # return HttpResponse("this is the equivalent of authorsid!")
    return render(request, 'BooksAuthorsApp/authors.html', context) 
