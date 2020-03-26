from django.test import TestCase
from books.models import Book, BookTag
from books.views import bring_books
from books.tests.base_cases import book_case_1
import mock

class BookViewTestCase(TestCase):
    @mock.patch('books.views.Book.objects.all')
    def test_book_view(self, mock_book_objects_all):
        mock_book_objects_all.return_value = (book_case_1,)
        response = self.client.get(
            "/books",
        ) #example of how to patch a method but in this case is useless
        self.assertEqual(response.status_code, 301)
