from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^message/$', views.message, name='message'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^protected/$', views.protected, name='protected'),
    url(r'^moban/$', views.moban, name='moban'),
]
