from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^results/$', views.article_search, name="search"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.article_edit, name="edit"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.article_delete, name="delete"),

]