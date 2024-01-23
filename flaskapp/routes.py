from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import forms_register, forms_login
from flaskapp.models import User, Post

posts = [
    {
        'author': 'Test User 1',
        'title': 'Test Title 1',
        'content': 'Test Content 1',
        'date_posted': 'Test Date 1',
    },
    {
        'author': 'Test User 2',
        'title': 'Test Title 2',
        'content': 'Test Content 2',
        'date_posted': 'Test Date 2',
    }
]

@app.route("/")
def routes_home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def routes_register():
    form = forms_register()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('routes_home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def routes_login():
    form = forms_login()
    if form.validate_on_submit():
        if form.email.data == "123@test.com" and form.password.data == "123":
            flash(f'{form.username.data} have been logged in!', 'success')
            return redirect(url_for('routes_home'))
        else:
            flash('Login failed.', 'danger')
    return render_template('login.html', title='Register', form=form)
