from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from .models import Article
from .views import index

