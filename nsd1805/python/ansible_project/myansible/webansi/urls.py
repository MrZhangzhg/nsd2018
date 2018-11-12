from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^addhosts/$', views.add_hosts, name='addhosts'),
    url(r'^delhost/(?P<host_id>\d+)/$', views.del_host, name='delhost'),
    url(r'^addmodules/$', views.add_modules, name='addmodules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
]

