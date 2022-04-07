from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user,current_user,login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {"author": {'username':'John'},
         'body':'The Avengers movie was so cool!'},
        {"author": {'username': 'Susan'},
         'body': 'Beautiful day in Portland!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():

        flash('Login Succeed for user {}, remember_me={}').format(form.username.data,form.remember_me.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
