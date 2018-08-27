from django.shortcuts import render
from django.utils import timezone
from .models import Contents

def post_list(request):
    posts = Contents.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def result(request):
    d = {
        'c1val': request.GET.get('c1val'),
        'c2val': request.GET.get('c2val'),
        'c3val': request.GET.get('c3val'),
        'c4val': request.GET.get('c4val'),

    }
    return render(request, 'blog/result.html', d)

def sum(request):
   d = {
       'c1val': request.GET.get('c1val')
   }

   return render(request, 'blog/result.html', d)
