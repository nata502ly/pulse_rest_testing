import unittest
from pulse_rest_client import PulseRestAPI
from models import Book


class BookCreationTests(unittest.TestCase):
    def setUp(self):
        self.app = PulseRestAPI("books")

    def test_book_creation(self):
        book = Book(title="New book", author="Super author")
        response = self.app.create_object(book)
        # Verification
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(response.json(), book.get_dict_with_id())
