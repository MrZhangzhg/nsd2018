from django.shortcuts import render, HttpResponse

def index(request):
    # 把polls/index.html网页发送给用户,存在polls/templates下
    return render(request, 'polls/index.html')

def hello(request):
    return render(request, 'polls/hello.html')

def detail(request, question_id):
    # return HttpResponse('你正在查看第%s个问题' % question_id)
    return render(request, 'polls/detail.html', {'q': question_id})
    # 字典的key相当于变量名，value相当于是变量值，传递给模板文件

def result(request, question_id):
    return HttpResponse('你正在查看第%s个问题的结果' % question_id)

def vote(request, question_id):
    return HttpResponse('你正在为第%s个问题投票' % question_id)

