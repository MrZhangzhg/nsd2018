from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, {'age': 23}, name='hello'),
    url(r'^(?P<name>[a-zA-Z]+)/(?P<age>\d+)/', views.info, name='info'),
]
