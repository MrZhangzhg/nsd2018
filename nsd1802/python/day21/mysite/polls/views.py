from django.shortcuts import render

def index(request):
    # 把index.html网页发送给用户
    return render(request, 'polls/index.html')

