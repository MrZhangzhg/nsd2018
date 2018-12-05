from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='polls_index'),
    url(r'^addhosts/$', views.addhosts, name='addhosts'),
    url(r'^addmodules/$', views.addmodules, name='addmodules'),
]
