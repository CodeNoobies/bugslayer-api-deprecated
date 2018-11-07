from django.urls import path
from .views import index, show

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', show, name='show_article'),
]
