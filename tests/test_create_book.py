import pytest
from models.book import Book

test_data = [
    Book(title='0', author='1'),
    Book(title="New book", author="Super author")
]


@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_book_creation(app, book):
    response = app.create_object(book)
    # Verification
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()


def test_book_creation_no_author(app):
    book = Book(title="New book")
    response = app.create_object(book)
    # Verification
    assert response.status_code == 400
    # assert response.json() == book.get_dict_with_id()

