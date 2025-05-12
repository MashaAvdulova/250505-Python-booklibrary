class LibraryInterface:
    def __init__(self, library):
        self.library = library
        self.user_action = None
        self.text_menu = ('Добро пожаловать в библиотеку\n'
                          'Выбарите нужный пункт меню (от 0 до 5)\n'
                          '1. Посмотреть все книги\n'
                          '2. Добавить книгу\n'
                          '3. Показать количество книгу\n'
                          '4. Поиск книг по названию\n'
                          '5. Поиск книг по автору\n'
                          '6. Проверить статус книги\n'
                          '-------------------\n'
                          '0. Выйти из программы\n'
                          )

    def print_main_menu(self):
        print(self.text_menu)
        self.user_action = input('>>> ')
        self.process_main_menu()

    def process_main_menu(self):
        while True:
            match self.user_action:
                case '1':
                    books = self.library.book_list()
                    if books:
                        print('Список книг:')
                        self.print_books(books)
                        self.print_main_menu()
                    else:
                        print('Книг нет')
                        self.print_main_menu()
                case '2':
                    self.add_book()
                    self.print_main_menu()
                case '3':
                    pass
                    # показать количество книг
                case '4':
                    pass
                    # показать количество книг
                case '5':
                    self.find_books_by_author()
                    self.print_main_menu()



    def print_books(self, books):
        for book in books:
            print(f'ID - {book}')
            print(f'Автор - {books[book]["author"]}')
            print(f'Название - {books[book]["title"]}')
            print(f'Год издания - {books[book]["year"]}')
            print(f'Статус - {books[book]["status"]}')
            print('--------------')

    def add_book(self):
        author = input('Введите автора книги:\n>>> ')
        title = input('Введите название книги:\n>>> ')
        year = input('Введите год издания книги:\n>>> ')
        try:
            self.library.book_add(author=author, title=title, year=year)
            print('Книга успешно добавлена')
        except Exception as err:
            print(f'Возникла проблема {err}')

    def find_books_by_author(self):
        author = input('Введите автора книги:\n>>> ')
        books = self.library.find_book_by_author(author=author)
        if books:
            print('Результат поиска:')
            self.print_books(books)
        else:
            print('По вашему запросу ничего не найдено')



        # if self.user_action == '1':
        #     print('Вызвана функция "Посмотреть все книги"')
        # elif self.user_action == '2':
        #     print('Вызвана функция "Добавить книгу"')
        # else:
        #     print('Выберите нужный пункт меню')
