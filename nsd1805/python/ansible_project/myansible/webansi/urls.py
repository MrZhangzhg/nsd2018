from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^addhosts/$', views.add_hosts, name='addhosts'),
]

