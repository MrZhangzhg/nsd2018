from django.shortcuts import render, HttpResponse

def polls_index(request):
    # return HttpResponse('<h1>Polls index</h1>')
    return render(request, 'polls/polls_index.html')