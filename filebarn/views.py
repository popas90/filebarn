from flask import render_template, flash, redirect
from flask import session, url_for, request, g
from flask.ext.login import login_user, logout_user
from flask.ext.login import current_user, login_required
from filebarn import app, db, lm
from .forms import LoginForm
from .models import User


@app.route('/secret/<username>')
@login_required
def secret(username):
    return render_template('index.html', username=username)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or
                            url_for('secret', username=form.username.data))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
