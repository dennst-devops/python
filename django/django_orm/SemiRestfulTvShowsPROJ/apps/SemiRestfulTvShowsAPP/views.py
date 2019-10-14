from django.shortcuts import render

# Create your views here.
#-#-#-#-#-#-#-#-#-#-
# apps views.py (4)
#-#-#-#-#-#-#-#-#-#-

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")