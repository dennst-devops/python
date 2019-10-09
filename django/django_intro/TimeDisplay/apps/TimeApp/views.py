from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from time import gmtime, strftime, localtime
import datetime

#-#-#-#-#-#-#-#-#-#-
# apps views.py (4)
#-#-#-#-#-#-#-#-#-#-
# Create your views here.
def index(request):
    context = {
        "time": strftime("%H:%M:%S", localtime()),
        "date": strftime("%Y-%m-%d", localtime())
    }
    return render(request,'TimeApp/index.html', context)