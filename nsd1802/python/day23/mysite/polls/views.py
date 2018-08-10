from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question

def index(request):
    # 把polls/index.html网页发送给用户,存在polls/templates下
    qlist = Question.objects.order_by('-pub_date')[:5]
    context = {'qlist': qlist}
    return render(request, 'polls/index.html', context)

def hello(request):
    return render(request, 'polls/hello.html')

def detail(request, question_id):
    # return HttpResponse('你正在查看第%s个问题' % question_id)
    # q = Question.objects.get(id=question_id)
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'q': q})
    # 字典的key相当于变量名，value相当于是变量值，传递给模板文件

def result(request, question_id):
    # return HttpResponse('你正在查看第%s个问题的结果' % question_id)
    q = Question.objects.get(id=question_id)
    return render(request, 'polls/result.html', {'q': q})

def vote(request, question_id):
    # return HttpResponse('你正在为第%s个问题投票' % question_id)
    q = Question.objects.get(id=question_id)
    c = q.choice_set.get(id=request.POST['choice'])
    c.votes += 1
    c.save()
    # 重定向到urls.py中定义的name='result'那个网址
    return redirect('result', question_id=question_id)

# 登陆面面
def home(request):
    return render(request, 'polls/home.html')

# 验证用户是否登陆成功
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    if username == 'bob' and password == '123456':
        request.session['IS_LOGIN'] = True
        return redirect('index')
    return redirect('home')

# 已登陆用户可以访问，如果没有登陆，重定向到登陆页面
def protected(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        return HttpResponse('OK')
    return redirect('home')

def mytest(request):
    i = 10
    alist = ['bob', 'alice']
    adict = {'name': 'tom', 'age': 25}
    context = {'i': i, 'alist': alist, 'adict': adict}
    return render(request, 'polls/mytest.html', context)
