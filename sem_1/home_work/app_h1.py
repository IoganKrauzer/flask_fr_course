from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/news/')
def news():
    news_list = [
        {
            'news_title': 'News_title_str_1',
            'news_text': 'Lorem_str_1',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {
            'news_title': 'News_title_str_2',
            'news_text': 'Lorem_str_2',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {
            'news_title': 'News_title_str_3',
            'news_text': 'Lorem_str_3',
            'date': datetime.now().strftime('%H:%M - %m.%d.%Y года')}]

    return render_template('news.html', news_list=news_list)


@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {
            'shoes_title': 'Shoes_title_str_1',
            'made_in': 'Made in_int_1',
            'year': 'Year_int_1'},
        {
            'shoes_title': 'Shoes_title_str_2',
            'made_in': 'Made in_int_2',
            'year': 'Year_int_2'},
        {
            'shoes_title': 'Shoes_title_str_3',
            'made_in': 'Made in_int_3',
            'year': 'Year_int_3'}]

    return render_template('shoes.html', shoes_list=shoes_list)


@app.route('/jacket/')
def jacket():
    jacket_list = [
        {
            'jacket_title': 'Jacket_title_str_1',
            'made_in': 'Made in_str_1',
            'year': 'Year_int_1',
            'size_jacket': 'size_jacket_int_1'},
        {
            'jacket_title': 'Jacket_title_str_2',
            'made_in': 'Made in_str_2',
            'year': 'Year_int_2',
            'size_jacket': 'size_jacket_int_2'},
        {
            'jacket_title': 'Jacket_title_str_3',
            'made_in': 'Made in_str_3',
            'year': 'Year_int_3',
            'size_jacket': 'size_jacket_int_3'}]

    return render_template('jacket.html', jacket_list=jacket_list)


if __name__ == '__main__':
    app.run(debug=True)
