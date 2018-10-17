from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice

# request必须提供，表示用户的请求
# def index(request):
#     return HttpResponse('<h1>Polls OK</h1>')

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    choice_id = request.POST.get('c_id')
    c = get_object_or_404(Choice, id=choice_id)
    c.votes += 1
    c.save()
    return redirect('result', question_id=question_id)
