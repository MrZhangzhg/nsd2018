from django.shortcuts import render, HttpResponse
from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    return HttpResponse('<h1>%s: detail</h1>' % question_id)
