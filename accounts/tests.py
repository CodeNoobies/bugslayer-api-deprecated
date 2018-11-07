import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.contrib.auth.models import User
from .serializers import UserSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        User.objects.create(username='jon', email='jon@doe.com', password='empanadas')
        self.valid_data = {
            'username': 'jane'
        }


class GetAllUsersTest(BaseViewTest):
    def test_get_all_users(self):
        """
        This test ensures that all the users added in the setUp
        method exist when we do a GET request to the articles endpoint
        """
        response = self.client.get(
            reverse('users-all')
        )

        expectedUsers = User.objects.all()
        serialized = UserSerializer(expectedUsers, many=True)
        self.assertEqual(response.data, serialized.data)
        #self.assertContains(response, 'article')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetUserDetailsTest(BaseViewTest):
    def test_get_user_details(self):
        """
        This test ensures we can successfully find the user
        we just created during the setUp
        """
        response = self.client.get(
            reverse(
                'user-details', kwargs={
                    'username': 'jon'
                }
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserDetailsTest(BaseViewTest):
    """
    This test ensures we can successfully update the user
    we created during the setUp
    """
    def test_update_user_details(self):
        response = self.client.put(
            reverse('user-details',
                kwargs={
                    'username': 'jon'
                }
            ),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(BaseViewTest):
    """
    This test ensures we can successfully delete the user
    we created during the setUp
    """
    def test_delete_user(self):
        response = self.client.delete(
            reverse('user-details',
                kwargs={
                    'username': 'jon'
                }
            )
        )
        self.assertAlmostEqual(response.status_code, status.HTTP_204_NO_CONTENT)

