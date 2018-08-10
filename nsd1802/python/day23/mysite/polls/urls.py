from django.conf.urls import url
from . import views

urlpatterns = [
    # 当用户访问http://127.0.0.1/pools/就调用views.index函数
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, name='hello'),
    # [0-9]+匹配数字，?P<question_id>表示定义的变量名为question_id
    # 把匹配到的数字赋值给question_id，并传递给views.detail作为参数
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


