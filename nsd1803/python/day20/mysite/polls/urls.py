from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.polls_index, name='polls_index'),
    url(r'^(?P<q_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<q_id>\d+)/result/$', views.result, name='result'),
    url(r'^(?P<q_id>\d+)/vote/$', views.vote, name='vote'),
]
