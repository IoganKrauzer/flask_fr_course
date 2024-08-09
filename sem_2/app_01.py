"""
Задача 1:
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
from pathlib import Path, PurePath
from flask import Flask, render_template, request, abort, flash, redirect, url_for
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'035d6d165836a72a0180ea16a9cd27c8fb656bfa35e92f8a67467c15f39831ca'


# in Python Console
# >>> import secrets
# >>> secrets.token_hex()


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/next')
def next_page_1():
    return 'Привет, Вася'


@app.route('/load_image', methods=['GET', 'POST'])
def load_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {escape(file_name)} загружен на сервер"

    context = {
        'task': 'Задание 2'
    }
    return render_template('page_1.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    log_check = {
        'auth_email': '1@email.ru',
        'auth_pass': '123'
    }

    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')

        if auth_email == log_check['auth_email'] and auth_pass == log_check['auth_pass']:
            return f'Вход выполнен успешно'
        else:
            return f'Error!'

    context = {
        'task': 'Задание 3'
    }

    return render_template('page_login.html', **context)


@app.route('/count', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        text = request.form.get('text')

        return f'Кол-во слов {len(text.split())}'

    context = {
        'task': 'Задание 4'
    }

    return render_template('counter.html', **context)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    context = {
        'task': 'Задание 5'
    }
    if request.method == 'POST':
        num_1 = int(request.form.get('number_1'))
        num_2 = int(request.form.get('number_2'))
        operation = request.form.get('operations')
        match operation:
            case 'add':
                return f'{str(num_1 + num_2)}'
            case 'subtract':
                return f'{str(num_1 - num_2)}'
            case 'multiplication':
                return f'{str(num_1 * num_2)}'
            case 'division':
                try:
                    return f'{str(num_1 / num_2)}'
                except ZeroDivisionError as e:
                    return f'{e}'

    return render_template('calc_page.html', **context)


@app.errorhandler(403)
def page_not_found():
    context = {
        'title': 'Некорректный возраст',
        'url': request.base_url
    }

    return render_template('403.html', **context), 403


@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_age = int(request.form.get('user_age'))
        if user_age >= 18:
            return f'{user_name}: {str(user_age)} лет, он может пройти авторизацию'

        return abort(403)

    contex = {
        'task': 'Задача 6'}

    return render_template('check_age.html', **contex)


@app.route('/square/', methods=['GET', 'POST'])
def square_of_number():
    if request.method == 'POST':
        num = request.form.get('number')
        square_of_number_ = str(int(num) ** 2)
        return f'Число: {num} | Квадрат числа: {square_of_number_}'

    contex = {
        'task': 'Task 7'
    }
    return render_template('square_page.html', **contex)


@app.route('/flash', methods=['GET', 'POST'])
def flash_msg():
    if request.method == 'POST':
        if not request.form.get('surname'):
            flash('Input surname!')
            # return redirect(url_for('flash_msg'))

        if not request.form.get('firstname'):
            flash('Input name!')
            return redirect(url_for('flash_msg'))
        surname = request.form.get('surname')
        name = request.form.get('firstname')
        return redirect(url_for('authorization', name=name, surname=surname))
        # flash(f'Привет, {ppp}')
        # return redirect(url_for('flash_msg'))

    context = {
        'task': 'Task 8 '
    }

    return render_template('flash_page.html', **context)


@app.route('/authorization/<name>/')
def authorization(name):
    context = {
        'title': 'Authorization',
        'name': name,
    }
    return render_template('authorization_page.html', **context)


@app.route('/form', methods=['GET', 'POST'])
def flash_msg_2():

    if request.method == 'POST':

        if not request.form['firstname']:
            flash('Error!', category='danger')
            return redirect(url_for('flash_msg_2'))
        flash('Успешно введено имя!', category='success')
        return redirect(url_for('flash_msg_2'))

    return render_template('flash_page_2.html')


if __name__ == '__main__':
    AGE_LIMIT = 18
    app.run(debug=True)
