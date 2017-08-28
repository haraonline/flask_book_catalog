from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if current_user.is_authenticated:
        flash('you are already registered')
        return redirect(url_for('main.display_books'))
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration Successful')
        return redirect(url_for('authentication.do_the_login'))
    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def do_the_login():
    if current_user.is_authenticated:
        flash('you are already logged-in')
        return redirect(url_for('main.display_books'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))
        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    flash('Logged out Successfully')
    return redirect(url_for('main.display_books'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
