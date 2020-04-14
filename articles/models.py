from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)    
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'