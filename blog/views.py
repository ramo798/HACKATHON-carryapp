from django.shortcuts import render
from django.utils import timezone
from .models import Contents
from .models import Naiyou
import random

def post_list(request):
    posts = Contents.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def result(request):
    a = int( request.GET.get('c1val') )
    b = int( request.GET.get('c2val') )
    c = int( request.GET.get('c3val') )
    d = int( request.GET.get('c4val') )
    sum = a + b + c + d
    if sum != 0:
        w1 = float(a/sum)
        w2 = float(b/sum)
        w3 = float(c/sum)
        w4 = float(d/sum)

    if sum == 0:
        w1 = 0.1
        w2 = 0.1
        w3 = 0.1
        w4 = 0.1





    y = [1,2,3]
    g = [4,5,6]
    r = [7,8,9]
    b = [10,11,12]

    if sum == 0:
        kekka = y + g + r + b

    if w1 < 0.2 :
        br = [0]
    if 0.19 < w1 < 0.30 :
        br = [random.choice(b)]
    if 0.29 < w1 < 0.40 :
        br = random.sample(b,2)
    if w1 > 0.39 :
        br = random.sample(b,3)

    if w2 < 0.2 :
        yr = [0]
    if 0.19 < w2 < 0.30 :
        yr = [random.choice(y)]
    if 0.29 < w2 < 0.40 :
        yr = random.sample(y,2)
    if w2 > 0.39 :
        yr = random.sample(y,3)

    if w3 < 0.2 :
        rr = [0]
    if 0.19 < w3 < 0.30 :
        rr = [random.choice(r)]
    if 0.29 < w3 < 0.40 :
        rr = random.sample(r,2)
    if w3 > 0.39 :
        rr = random.sample(r,3)

    if w4 < 0.2 :
        gr = [0]
    if 0.19 < w4 < 0.30 :
        gr = [random.choice(g)]
    if 0.29 < w4 < 0.40 :
        gr = random.sample(g,2)
    if w4 > 0.39 :
        gr = random.sample(g,3)
    if sum != 0:
        kekka = yr+gr+rr+br


    if 0 in kekka :
        kekka.remove(0)
    if 0 in kekka :
        kekka.remove(0)
    if 0 in kekka :
        kekka.remove(0)
    if 0 in kekka :
        kekka.remove(0)

    ijou = random.choice(kekka)


    posts = Contents.objects.filter(id = ijou)
    mozi = Naiyou.objects.filter(id = ijou)
    d = {
        'test': ijou,
        'posts': posts,
        'mozi': mozi,
    }
    return render(request, 'blog/result.html', d)

def sum(request):
   d = {
       'c1val': request.GET.get('c1val')
   }

   return render(request, 'blog/result.html', d)
