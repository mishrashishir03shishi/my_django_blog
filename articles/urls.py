from django.conf.urls import url
from .import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.article_list.as_view(), name="list"),
    path('results/', views.article_search, name="search"),
    path('about/', views.about, name="about"),
    path('create/', views.article_create.as_view(), name="create"),
    path('<int:pk>/', views.article_detail.as_view(), name="detail"),
    path('<int:pk>/edit/',views.article_edit.as_view(), name="edit"),
    path('<int:pk>/delete/', views.article_delete.as_view(), name="delete"),

]