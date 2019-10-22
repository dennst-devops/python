#-#-#-#-#-#-#-#-#-#-
# BeltPrepAPP  urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to BeltPrepPROJ/apps/BeltPrepAPP/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # landing pages
    url(r'^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^books/new', views.newbook),
    url(r'^books/(?P<ht_bookid>\d+)', views.viewbookdetails),
    url(r'^books/edit/(?P<ht_bookid>\d+)', views.editbook),

    # process routes
    url(r'^register_process', views.register_process),
    url(r'^login_process', views.login_process),
    url(r'^logout_process', views.logout_process),
    url(r'^createnewbook_process', views.createnewbook_process),
    url(r'^books/update/(?P<ht_bookid>\d+)', views.update_process),
    url(r'^books/delete/(?P<ht_bookid>\d+)', views.delete_process),
]