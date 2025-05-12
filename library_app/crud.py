import json

class LibraryCRUD:
    # получение книги по id
    def get_book_by_id(self, session, book_id):
        # перемещаем указатель файла в начало
        session.seek(0)
        # считывание файла в переменную data (словарь)
        data = json.loads(session.read())
        # получаем вложенный словарь
        books = data.get('library', {}).get('books',{})
        # получаем конкретную книгу
        book = books.get(book_id)
        return book

    # Получение словаря со всеми книгами
    def book_list(selfself,session):
        # перемещаем указатель файла в начало
        session.seek(0)
        # считывание файла в переменную  data (словарь)
        data = json.loads(session.read())
        # получаем вложенный словарь с книгами
        books = data.get('library', {}).get('books', {})
        return books

    # Получение книг одного автора
    def get_books_by_author(self, session, author):
        # перемещаем указатель файла в начало
        session.seek(0)
        # считывание файла в переменную  data (словарь)
        data = json.loads(session.read())
        # получаем вложенный словарь с книгами
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books: # book - id книги
            if books[book] ['author'].lower().find(author.lower()) != -1:
                result[book] = books[book]
        return result

    # DZ
    def get_books_by_title(self):
        pass

    # Добавление  книги
    def book_add(selfself, session, bool_id, aythor, title,year):
        # перемещаем указатель файла в начало
        session.seek(0)
        # считывание файла в переменную  data (словарь)
        data = json.loads(session.read())
        book_object = {
            bool_id: {
                'author': aythor,
                'title':title,
                'year':year,
                'status': 'В наличии'
            }
        }
        data['library']['books'].update(book_object)
        # перемещаем указатель файла в начало, чтобы все стереть и записать новые данные
        session.seek(0)
        json.dump(data, session, indent=2, ensure_ascii=False)
        return True

crud = LibraryCRUD()