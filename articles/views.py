from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from .models import Article
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied


class article_list(ListView):
    model = Article
    template_name='articles/article_list.html'
    context_object_name = 'post'
    paginate_by=3
    
#@login_required(login_url="/accounts/login/")
class article_detail(LoginRequiredMixin,DetailView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_detail.html'
    # return HttpResponse(slug)
   

#@login_required(login_url="/accounts/login/")
class article_create(LoginRequiredMixin,CreateView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_create.html'    
    fields=['title','body','thumb'] 

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


#@login_required(login_url="/accounts/login/")
class article_edit(LoginRequiredMixin,UpdateView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_edit.html'
    fields=['title','body','thumb']   

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


#@login_required(login_url="/accounts/login/")
class article_delete(LoginRequiredMixin,DeleteView):
    login_url='/accounts/login/'
    model=Article
    template_name='articles/article_delete.html'
    success_url=reverse_lazy('articles:list')

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

def article_search(request):
    query=request.GET.get('q')
    post = Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))    
    return render(request, 'articles/article_list.html', { 'post': post } )

def about(request):
    return render(request, 'articles/about.html')