from django.conf.urls import url
from . import views

urlpatterns = [
    # 当用户访问http://127.0.0.1/pools/就调用views.index函数
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, name='hello')
]


