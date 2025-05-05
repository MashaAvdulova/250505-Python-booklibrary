from library_app.db import Session

def main():
    session = Session.session_maker() # Session.db_file даст тот же результат, но принято через функцию

if __name__ == '__main__':
    main()

