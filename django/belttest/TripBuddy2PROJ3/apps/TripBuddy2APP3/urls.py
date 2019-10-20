#-#-#-#-#-#-#-#-#-#-
# TripBuddy2APP3  urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to TripBuddy2PROJ3/apps/TripBuddy2APP3/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # landing pages
    url(r'^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^trips/new', views.new),
    url(r'^trips/(?P<ht_tripid>\d+)', views.viewtripdetails),
    url(r'^trips/edit/(?P<ht_tripid>\d+)', views.edittrip),

    # process routes should all have process in the name if they do validations
    url(r'^register_process', views.register_process),
    url(r'^logout', views.logout),
    url(r'^login_process', views.login_process),
    url(r'^createnewtrip_process', views.createnewtrip_process),
    url(r'^trips/delete/(?P<ht_tripid>\d+)', views.delete),
    url(r'^trips/edit/(?P<ht_tripid>\d+)', views.edit_process),
    url(r'^trips/update/(?P<ht_tripid>\d+)', views.edit_process),
]