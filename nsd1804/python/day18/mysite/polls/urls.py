from django.conf.urls import url
from . import views  # django默认把项目基础目录设置为mysite(manage.py所在目录)

urlpatterns = [
    # 使用index函数响应polls主页请求，该url的名字(name)是index
    url(r'^$', views.index, name='index'),  # http://127.0.0.1/polls/
    url(r'(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'(?P<question_id>\d+)/result/$', views.result, name='result'),
    url(r'(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]
