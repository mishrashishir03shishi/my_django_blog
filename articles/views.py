from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })
    
@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })


@login_required(login_url="/accounts/login/")
def article_edit(request,slug):
    article=Article.objects.get(slug=slug)
    form = forms.CreateArticle(instance=article)
    Article.objects.filter(slug=slug).delete()
    if request.method == 'POST':        
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')    
    return render(request, 'articles/article_create.html', { 'form': form })


@login_required(login_url="/accounts/login/")
def article_delete(request,slug):
    Article.objects.filter(slug=slug).delete()
    return render(request,'articles/article_delete.html')

def article_search(request):
    query=request.GET.get('q')
    articles = Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))    
    return render(request, 'articles/article_list.html', { 'articles': articles } )
