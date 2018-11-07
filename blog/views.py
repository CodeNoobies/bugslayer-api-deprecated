from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    """
    Returns a list of the articles with published status.
    """
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

def show(request, slug):
    """
    Returns a single article or 404 based on the slug passed as argument.
    """
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})
