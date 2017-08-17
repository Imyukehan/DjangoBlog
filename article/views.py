from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# Show homepage
def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage: 
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})
# Show article
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
# Show archive
def archive(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archive.html', {'post_list': post_list, 'error': False})
# Show about me
def about_me(request):
    return render(request, 'aboutme.html')
# Show by tags
def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

# add search function
def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archive.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archive.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')