from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from .models import Article
from .views import index

"""
class IndexTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Jon', email='jon@doe.com', password='jondoe')
        self.article = Article.objects.create(title='Test Article', content='Just a test article', author=self.user)
        url = reverse('index')
        self.response = self.client.get(url)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)
"""
