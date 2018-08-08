from django.shortcuts import render

def index(request):
    # 把polls/index.html网页发送给用户,存在polls/templates下
    return render(request, 'polls/index.html')

def hello(request):
    return render(request, 'polls/hello.html')

