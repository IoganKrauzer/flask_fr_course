import hashlib

from flask import Flask, request, render_template, redirect
from flask_wtf import CSRFProtect

from home_work.forms import RegisterForm
from home_work.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///hw_users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Home_work --- OK')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        user_first_name = form.first_name.data
        user_surname = form.surname.data
        user_email = form.email.data
        user_password = form.password.data
        user = User(
            first_name=user_first_name,
            surname=user_surname,
            email=user_email,
            password=user_password
        )
        user.set_password(user_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template('register_page.html', form=form)


@app.route('/users/')
def get_all_users():
    users = User.query.all()
    contex = {
        'users': users
    }
    return render_template('users_page.html', **contex)
