from flask import Flask, render_template
from task_2.models import db, Book, Author, BookAuthor
from random import randint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_book.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Task #2 --- OK')


@app.cli.command("add-data")
def add_data():
    for i in range(1, 11):
        book = Book(
            name=f'Book{i}',
            year_publishing=randint(1950, 2024),
            number_of_copies=randint(500, 2500),
        )
        db.session.add(book)

    for i in range(1, 16):
        author = Author(
            name=f'AuthorName{i}',
            surname=f'AuthorSurname{i}',
        )
        db.session.add(author)

    for i in range(10):
        book_author = BookAuthor(
            book_id=randint(1, 10),
            author_id=randint(1, 15)
        )
        db.session.add(book_author)
    db.session.commit()
    print('Данные добавлены #2')


@app.route('/book/')
def get_books():
    books = Book.query.all()
    context = {
        'books': books
    }
    return render_template('books_page.html', **context)
