from django.conf.urls import url
from hellow import views
urlpatterns=[url(r'^$',views.index,name='home'),]
