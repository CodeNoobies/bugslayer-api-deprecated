from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(max_length=5000, null=False)
    # Set null in case the user gets deleted, just assume it was posted by
    # someone anonymous
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title
