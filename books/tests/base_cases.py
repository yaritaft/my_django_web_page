from books.models import Book, BookTag
from django.utils.timezone import now


book_case_1=Book(
    title='my_test_book',
    created_date=now(),
    updated_date=now(),
    summary="Lorem ipsum ha ha ha",
    rate=9,
    link='http://127.0.0.1',
    author='Freddy Krugger',
    edition='3rd'
)

book_case_2_dict={
    "title": 'my_test_book_v2',
    "summary": "_v2Lorem ipsum ha ha ha",
    "rate": 9,
    "link": 'http://127.0.0.1',
    "author": '_v2Freddy _v2Krugger',
    "edition": '_v23rd'
}