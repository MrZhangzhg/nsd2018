from django.shortcuts import render, HttpResponse
from .models import Question

def polls_index(request):
    # return HttpResponse('<h1>Polls index</h1>')
    # return render(request, 'polls/polls_index.html')
    # 按发布日期降序排列，取最新的5个问题
    latest_qlist = Question.objects.order_by('-publish_date')[:5]
    context = {'qlist': latest_qlist}
    return render(request, 'polls/polls_index.html', context)

def detail(request, q_id):
    # return HttpResponse('你正在查看第%s个问题' % q_id)
    return render(request, 'polls/detail.html', {'question_id': q_id})

def result(request, q_id):
    return render(request, 'polls/result.html', {'question_id': q_id})

def vote(request, q_id):
    pass
