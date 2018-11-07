from django.urls import path
from blog.views import ListArticlesView


urlpatterns = [
    path('', ListArticlesView.as_view(), name='articles-all'),
]
