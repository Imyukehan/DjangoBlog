from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
# Show homepage
def home(request):
    post_list = Article.objects.all()
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