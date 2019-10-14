
#-#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to your_PROJECT_name_here/apps/your_APP_name_here/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]