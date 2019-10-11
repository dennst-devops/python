
#-#-#-#-#-#-#-#-#-#-
# apps urls.py (3)
#-#-#-#-#-#-#-#-#-#-
#add all to your_PROJECT_name_here/apps/your_APP_name_here/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<ht_showbook>\d+)$', views.bookid),
    url(r'^addbook$', views.addbook),
    url(r'^addauth$', views.addauth),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<ht_showauth>\d+)$', views.authorsid),
]

