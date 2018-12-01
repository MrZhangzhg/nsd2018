from django.shortcuts import render, redirect
from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')
    choice = question.choice_set.get(id=choice_id)
    choice.vote += 1
    choice.save()

    return redirect('result', question_id=question_id)
