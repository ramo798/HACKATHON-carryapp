from django.shortcuts import render
from django.utils import timezone
from .models import Contents
from .models import Naiyou

def post_list(request):
    posts = Contents.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def result(request):
    a = int( request.GET.get('c1val') )
    b = int( request.GET.get('c2val') )
    c = int( request.GET.get('c3val') )
    d = int( request.GET.get('c4val') )

    if a > b and a > c and a > d :
        posts = Contents.objects.filter(id = 1)
        mozi = Naiyou.objects.filter(id = 1)
        url = "{% static 'pic/curry_indian_man.png' %}"
        #url = "static 'pic/curry_indian_man.png' "
    if b > a and b > c and b > d :
        posts = Contents.objects.filter(id = 2)
    if c > a and c > b and c > d :
        posts = Contents.objects.filter(id = 3)
    if d > a and d > b and d > c :
        posts = Contents.objects.filter(id = 4)
    if a+b+c+d == 0 :
        posts = Contents.objects.filter(id = 1)




    #posts = Contents.objects.filter(id = 1)
    d = {
        'test': a+b+c+d,
        'posts': posts,
        'url': url,
        'mozi': mozi,


    }
    return render(request, 'blog/result.html', d)

def sum(request):
   d = {
       'c1val': request.GET.get('c1val')
   }

   return render(request, 'blog/result.html', d)
