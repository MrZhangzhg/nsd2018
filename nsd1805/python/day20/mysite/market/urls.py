from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^protected/$', views.protected, name='protected'),
    url(r'^login/$', views.login, name='login'),
]


