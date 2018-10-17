from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question

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


