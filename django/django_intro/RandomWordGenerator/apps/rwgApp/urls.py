#-#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
#-#-#-#-#-#-#-#-#-#-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.rwg),
    url(r'^generate$', views.generate),
    url(r'^reset$', views.reset),
]