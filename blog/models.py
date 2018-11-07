from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(max_length=5000, null=False)
    slug = models.SlugField(max_length=255, unique_for_date='created_at')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
