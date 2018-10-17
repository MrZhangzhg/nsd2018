from django.shortcuts import render, HttpResponse
from .models import Question

# request必须提供，表示用户的请求
# def index(request):
#     return HttpResponse('<h1>Polls OK</h1>')

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

