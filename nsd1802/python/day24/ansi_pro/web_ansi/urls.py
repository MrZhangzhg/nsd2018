from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^exec_tasks/$', views.exec_tasks, name='exec_tasks'),
]
