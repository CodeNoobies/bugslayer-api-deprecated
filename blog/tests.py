from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Article
from .serializers import ArticleSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpwd')
        self.create_article('article test #1', 'this is the test #1')
        self.create_article('article test #2', 'this is the test #2')

    @staticmethod
    def create_article(self, title="", content=""):
        if title != "" and content != "":
            Article.objects.create(title=title, content=content, author=self.user)


class GetAllArticlesTest(BaseViewTest):
    def test_get_all_articles(self):
        """
        This test ensures that all the articles added in the setUp
        method exist when we do a GET request to the articles endpoint
        """
        response = self.client.get(
            reverse('articles-all')
        )

        expectedArticles = Article.objects.all()
        serialized = ArticleSerializer(expectedArticles, many=True)
        self.assertEqual(response.data, serialized.data)
        #self.assertContains(response, 'article')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
