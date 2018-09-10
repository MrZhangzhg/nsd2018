from django.shortcuts import render, HttpResponse

def polls_index(request):
    # return HttpResponse('<h1>Polls index</h1>')
    return render(request, 'polls/polls_index.html')

def detail(request, q_id):
    # return HttpResponse('你正在查看第%s个问题' % q_id)
    return render(request, 'polls/detail.html', {'question_id': q_id})
