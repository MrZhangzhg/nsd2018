from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='polls_index'),
]
