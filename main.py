from library_app.db import Session
from library_app import LibraryApp, LibraryInterface


def main():
    session = Session.session_maker() # Session.db_file даст тот же результат, но принято через функцию
    library = LibraryApp(session)
    interface = LibraryInterface(library)
    interface.print_main_menu()


if __name__ == '__main__':
    main()

