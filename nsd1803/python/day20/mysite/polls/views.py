from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Question, Choice

def polls_index(request):
    # return HttpResponse('<h1>Polls index</h1>')
    # return render(request, 'polls/polls_index.html')
    # 按发布日期降序排列，取最新的5个问题
    latest_qlist = Question.objects.order_by('-publish_date')[:5]
    context = {'qlist': latest_qlist}
    return render(request, 'polls/polls_index.html', context)

def detail(request, q_id):
    # return HttpResponse('你正在查看第%s个问题' % q_id)
    # question = Question.objects.get(pk=q_id)
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, q_id):
    # question = get_object_or_404(Question, pk=q_id)
    c_id = request.POST.get('c_id')
    # choice = question.choice_set.get(pk=c_id)
    choice = Choice.objects.get(pk=c_id)
    choice.votes += 1
    choice.save()
    return redirect('result', q_id=q_id)  # redirect不携带参数，访问新网页
