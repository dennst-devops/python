
#-#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to your_PROJECT_name_here/apps/your_APP_name_here/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addnew$', views.addnew),
    url(r'^allshows$', views.allshows),
    url(r'^editshows$', views.editshows),
    url(r'^showdetails$', views.showdetails),
    url(r'^destroy$', views.destroy),
]