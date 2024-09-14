from rest_framework.test import APITestCase
from rest_framework import status

class BookTests(APITestCase):
    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 4)  # Adjust based on your test data

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '1234567890',
            'cover': 'http://example.com/newcover.jpg'
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
