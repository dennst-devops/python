from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
# -#-#-#-#-#-#-#-#-#-
# apps views.py (4)
# -#-#-#-#-#-#-#-#-#-
from django.shortcuts import render, HttpResponse

def index(request):
    print("in index")
    # return HttpResponse("<h1>Visit <a href='http://localhost:8000/random_word'>here</a> for a random word!</h1>")
    return redirect('/random_word')

def rwg(request):
    request.session['randword'] = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    print(request.session['randword'])
    print(request.session['counter'])
    context = {
        "dj_counter": request.session['counter'],
        "dj_rndwrd": request.session['randword']
    }
    return render(request, 'rwgApp/index.html', context)

def reset(request):
    request.session['counter'] = 0
    print("in reset")
    return redirect('/random_word') 

def generate(request):
    print("in generate")
    return redirect('/random_word')
