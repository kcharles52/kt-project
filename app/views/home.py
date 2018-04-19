from flask import Blueprint, render_template, request, redirect, flash, url_for
from .forms import RegisterForm, LoginForm
from passlib.hash import sha256_crypt
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators, TextField
#from wtforms.validators import DataRequired, Length, EqualTo

home = Blueprint('home',__name__)



@home.route('/')
@home.route('/index')
def index():
    return render_template('home/index.html')

@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/register')
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))


        flash('You are now registered, you can log in', 'success')

        return redirect(url_for('login'))

    return render_template('/home/register.html', form=form)

#User login


@home.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        #gettting form fields
        username = request.form['username']
        password_entered = request.form['password']

        

    return render_template('/home/login.html', form=form)
