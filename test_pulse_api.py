import pytest
from pulse_rest_client import PulseRestAPI
from models import Book

@pytest.fixture()
def app():
    return PulseRestAPI(resource="books")


def test_book_creation(app):
    book = Book(title="New book", author="Super author")
    response = app.create_object(book)
    # Verification
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()
