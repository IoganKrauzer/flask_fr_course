from flask import Flask, render_template
from models import db, Student, Faculty
from random import randint, choice


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_data():
    for j in range(1, 4):
        faculty = Faculty(
            name=f'faculty{j}'
        )
        db.session.add(faculty)

    for i in range(1, 11):
        student = Student(
            firstname=f'Firstname{i}',
            surname=f'surname{i}',
            age=randint(16, 24),
            sex=choice(('female', 'male')),
            group=randint(1, 5),
            id_faculty=randint(1, 3)
        )
        db.session.add(student)
    db.session.commit()
    print('Данные добавлены')


@app.route('/')
def get_students():
    students = Student.query.all()
    context = {
        'students': students
    }
    return render_template('students_page.html', **context)
