from flask import Flask, render_template, redirect
from flask_wtf import CSRFProtect
from task_4.models import db, User
from flask import render_template, request
from task_4.forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Task #4 --- OK')


@app.route('/')
def get_users():
    users = User.query.all()

    contex = {
        'users': users
    }
    return render_template('users_page.html', **contex)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        user_name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=user_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template('register_page.html', form=form)
