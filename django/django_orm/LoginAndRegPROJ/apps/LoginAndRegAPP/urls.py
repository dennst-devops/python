#-#-#-#-#-#-#-#-#-#-
# LoginAndRegAPP  urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to LoginAndRegPROJ/apps/LoginAndRegAPP/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_process$', views.registration_process),
    url(r'^login_process$', views.login_process),
    #url(r'^success$', views.success),
    url(r'^clear_process$', views.clear_process),
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    #url(r'^delete/?P<commentid>\d+$', views.delete_comment),
]