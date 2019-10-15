from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
# Create your views here.
# -#-#-#-#-#-#-#-#-#-
# apps views.py (4)
# -#-#-#-#-#-#-#-#-#-

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'SemiRestfulTvShowsAPP/index.html')

def addshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    Show.objects.create(title=request.POST['ht_title'], network=request.POST['ht_network'], release_date=request.POST['ht_reldate'], desc=request.POST['ht_desc'])
    print(Show.objects.latest('id').id)
    dj_latestshow = Show.objects.latest('id').id
    return redirect(f'/shows/{dj_latestshow}')

def allshows(request):
    context = {
        "dj_allshows": Show.objects.all(),
    }
    # return HttpResponse("this is the equivalent of allshows!")
    return render(request, 'SemiRestfulTvShowsAPP/allshows.html', context)


def editshows(request, ht_showid):
    context = {
        "dj_showid": Show.objects.get(id=ht_showid),
    }
    return render(request, 'SemiRestfulTvShowsAPP/edit.html', context)


def showdetails(request, ht_showid):
    context = {
        "dj_showid": Show.objects.get(id=ht_showid),
    }
    # return HttpResponse("this is the equivalent of showdetails!")
    return render(request, 'SemiRestfulTvShowsAPP/showdetails.html', context)


def destroy(request, ht_showid):
    del_show = Show.objects.get(id=ht_showid)
    del_show.delete()
    return redirect('/shows')


def update(request, ht_showid):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{ht_showid}/edit')
    edit_show = Show.objects.get(id=ht_showid)
    edit_show.title = request.POST['ht_title']
    edit_show.network = request.POST['ht_network']
    edit_show.release_date = request.POST['ht_reldate']
    edit_show.desc = request.POST['ht_desc']
    edit_show.save()
    return redirect('/shows')
