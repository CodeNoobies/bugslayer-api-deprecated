from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer


class ListArticlesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
