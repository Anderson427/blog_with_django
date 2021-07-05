from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    ESTADO = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=ESTADO, default='rascunho')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
