import uuid
from .db import Session
from .crud import crud

class LibraryApp:
    """
    Основная бизнес-логика приложения
    """
    def __init__(self, session: Session):
        self.session = session
    # добавление книги
    def book_add(self, title, author, year):
        book_id = uuid.uuid4().hex[:10]
        title = title
        author = author
        year = year
        return crud.book_add(session=self.session, book_id=book_id, title=title, author=author, year=year)

    # список всех книг
    def book_list(self):
        books = crud.book_list(self.session)
        return books

    # удаление книги
    def book_delete(self, book_id):
        pass
        # book_id = validators.validate_book_id(self.session, book_id)
        # crud.get_book_by_id(self.session, book_id)
        # crud.book_delete(self.session, book_id)

    # получение статуса книги
    def get_book_status(self, book_id):
        pass
        # book_id = validators.validate_book_id(self.session, book_id)
        # book_status = crud.get_book_by_status(self.session, book_id)
        # return book_status

    #поиск книги по автору
    def find_book_by_author(self, author):
        pass
        books = crud.get_books_by_author(session=self.session, author=author)
        return books

    def find_book_by_title(self, title):
        books = crud.get_books_by_title(session=self.session, title=title)
        return books