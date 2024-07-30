from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    html_text = """
    <h1>Моя первая HTML страница</h1>
    <p>Привет, мир!</p>"""
    return html_text


@app.route('/world/')
def world():
    return render_template('index.html')


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/start/')
def start():
    return render_template('base.html')


@app.route('/about_new/')
def about_new():
    return render_template('about_new.html')


@app.route('/contact_new/')
def contact_new():
    return render_template('contact_new.html')


@app.route('/sum/<int:num_1>/<int:num_2>/')
def sum_f(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route('/lencheck/<string>/')
def str_len(string):
    return str(len(string))


@app.route('/students/')
def students():
    head = {
        'name': 'Name',
        'lastname': 'Last name',
        'age': 'Age',
        'rating': 'Average mark'
    }

    students_list = [
        {
            'name': 'Перий',
            'lastname': 'Валентайн',
            'age': 16,
            'rating': 84},
        {
            'name': 'Василий',
            'lastname': 'Васильянов',
            'age': 19,
            'rating': 74},
        {
            'name': 'Шиндо',
            'lastname': 'Хазурай',
            'age': 26,
            'rating': 88}]

    return render_template('students.html', **head, students_list=students_list)


@app.route('/news/')
def news():
    news_block = [
        {
            'title': 'news_1',
            'description': 'Description_1',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {
            'title': 'news_3',
            'description': 'Description_2',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {
            'title': 'news_2',
            'description': 'Description_3',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')}]

    return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
    app.run(debug=True)
