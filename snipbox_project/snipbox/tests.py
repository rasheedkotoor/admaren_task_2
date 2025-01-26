from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Snippet, Tag


class SnipBoxAPITestCase(APITestCase):

    def setUp(self):
        """
        Create a test user and authenticate.
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create a sample tag
        self.tag = Tag.objects.create(title="django")

        # Create a sample snippet
        self.snippet = Snippet.objects.create(
            title="Django REST",
            note="Testing Django REST API",
            created_by=self.user,
        )
        # Use tags.add() instead of passing directly in create()
        self.snippet.tags.add(self.tag)  # Attach tag properly

        # Obtain JWT token
        response = self.client.post('/auth/login/', {"username": "testuser", "password": "testpass"}, format="json")
        self.token = response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_snippets_overview(self):
        """
        Test listing all snippets.
        """
        response = self.client.get('/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_snippet(self):
        """
        Test creating a new snippet.
        """
        data = {
            "title": "New Snippet",
            "note": "This is a test snippet",
            "tags": [self.tag.id, ],
            "created_by": self.user.id,
        }
        response = self.client.post('/snippets/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Snippet")
