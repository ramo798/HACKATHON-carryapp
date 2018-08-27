from django.shortcuts import render
from django.utils import timezone
from .models import Contents

def post_list(request):
    posts = Contents.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def result(request):
    return render(request, 'blog/result.html', {})

def sum(request):
   d = {
       'sum': request.GET.get('sum')
   }

   return render(request, 'result.html', d)
