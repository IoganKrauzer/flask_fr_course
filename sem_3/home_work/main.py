import hashlib

from flask import Flask, request, render_template

from forms import RegistrationForm
from models import db, User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    pass

@app.route('/users/', methods=['POST', 'GET'])
def get_all_users():
    pass