# -#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
# -#-#-#-#-#-#-#-#-#-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process_money', views.process),
    url(r'^resetgold', views.resetgold),
    url(r'^reset$', views.reset),
    url(r'^', views.index),
]
