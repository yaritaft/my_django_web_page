from django.test import TestCase
from books.models import Book, BookTag
from django.db import IntegrityError
from books.views import from_query_set_to_dict
from books.tests.base_cases import book_case_1, book_case_2_dict


class BookTagTestCase(TestCase):
    def setUp(self):
        self.book_tag_1_str = 'python'
        self.book_tag_2_str = 'development'
        self.book_tag = BookTag(keyword=self.book_tag_2_str)
        self.book_tag.save()

    def test_create_a_book_tag(self):
        book_tag = BookTag(keyword=self.book_tag_1_str)
        book_tag.save()
        my_stored_book_tag = BookTag.objects.filter(
            keyword=self.book_tag_1_str).first()
        self.assertEqual(my_stored_book_tag, book_tag)

    def test_print_a_book_tag(self):
        my_stored_book_tag = BookTag.objects.filter(
            keyword=self.book_tag_2_str)
        self.assertNotEqual(len(my_stored_book_tag), 0)
        self.assertEqual(str(my_stored_book_tag.first()), self.book_tag_2_str)

    def test_unique_book_tag(self):
        """Animals that can speak are correctly identified"""
        book_tag = BookTag(keyword=self.book_tag_1_str)
        book_tag.save()
        book_tag_2 = BookTag(keyword=self.book_tag_1_str)
        self.assertRaises(IntegrityError, book_tag_2.save)


class BookTestCase(TestCase):
    def setUp(self):
        self.book_1 = book_case_1
        self.book_1.save()
        self.book_tag_3 = BookTag(keyword='horror')
        self.book_tag_3.save()
        self.book_2_dict = book_case_2_dict
        self.book_2 = Book(**self.book_2_dict)

    def test_print_book(self):
        self.assertEqual(
            str(self.book_1), 'my_test_book - Author:  Freddy Krugger')

    def test_relate_book_with_book_tag(self):
        self.book_1.tags.add(self.book_tag_3)
        my_stored_book = Book.objects.filter(title='my_test_book').first()
        self.assertEqual(my_stored_book.tags.first(), self.book_tag_3)

    def test_from_query_set_to_dict(self):
        self.assertEqual(
            self.book_2.__dict__, from_query_set_to_dict(self.book_2)
        )
