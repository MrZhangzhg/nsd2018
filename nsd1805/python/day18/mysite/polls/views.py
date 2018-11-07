from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request, 'index.html')
