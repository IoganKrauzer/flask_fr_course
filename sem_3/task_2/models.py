from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_book.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    year_publishing = db.Column(db.Integer, nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    # id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', secondary='book_author', backref='book', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.year_publishing}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
