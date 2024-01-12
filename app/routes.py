from app import app
from flask import render_template, url_for, flash, redirect, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/shop')
def shop():
    return render_template('shop.html', title='Shop')


@app.route('/account')
def account():
    return render_template('auth/login.html', title='Login')


# ---------------------
# Start: Auth
# ---------------------


@app.route('/request-password-reset')
def request_password_reset():
    return render_template('auth/request_password_reset.html', title='Request Password Reset')


@app.route('/reset-password')
def reset_password():
    return render_template('auth/reset_password.html', title='Reset Password')

# ---------------------
# Start: Auth
# ---------------------