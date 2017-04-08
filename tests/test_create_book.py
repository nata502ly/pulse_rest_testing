from models.book import Book


def test_book_creation(app):
    book = Book(title="New book", author="Super author")
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

