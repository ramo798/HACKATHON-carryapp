from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def result(request):
    return render(request, 'blog/result.html', {})
    
