
#-#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to your_PROJECT_name_here/apps/your_APP_name_here/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.allshows),
    url(r'^shows/new$', views.addshow),
    url(r'^shows/addshow$', views.addshow),
    url(r'^shows/(?P<ht_showid>\d+)/edit$', views.editshows),
    url(r'^shows/(?P<ht_showid>\d+)$', views.showdetails),
    url(r'^shows/(?P<ht_showid>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<ht_showid>\d+)/update$', views.update),
]