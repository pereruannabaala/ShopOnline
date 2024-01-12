from app import app
from flask import render_template, url_for, flash, redirect, request, session
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, CustomerRegistrationForm, AdminRegistrationForm, \
    AddToCart, ProductsForSaleForm, RequestPasswordResetForm, ResetPasswordForm
from app.models import Admin, Customer, User, ProductsForSale,\
    PurchasedProducts
from werkzeug.utils import secure_filename
import os
import requests
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/shop')
def shop():
    try:
        products = ProductsForSale.query.all()
        return render_template('shop.html', title='PRODUCTS LIST', products=products)
    except:
        products = None
        return render_template('shop.html', title='PRODUCTS LIST', products=products)


# ---------------------
# Start: Auth
# ---------------------

@app.route('/account', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer_checkout'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {user.username}')
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer_checkout'))
    # Cart items will go here

    return render_template(
        'auth/login.html',
        title='Login',
        form=form)


@app.route('/register/customer', methods=['GET', 'POST'])
def register_customer():
    if current_user.is_authenticated:
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer'))
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        user = Customer(
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            residence=form.residence.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully as customer. Please log in to continue')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)


@app.route('/logout')
@login_required
def logout():
    """Used to log out a user"""
    logout_user()
    return redirect(url_for('login'))


@app.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset():
    if current_user.is_authenticated:
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer_checkout'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user:
        #     send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template(
        'auth/request_password_reset.html',
        title='Request Password Reset',
        form=form)


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer_checkout'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template(
        'auth/reset_password.html',
        title='Reset Password',
        form=form)



# ---------------------
# End: Auth
# ---------------------


# ---------------------
# Start: Dashboard customer
# ---------------------

@app.route('/dashboard/customer/purchase-history', methods=['GET', 'POST'])
@login_required
def dashboard_customer():
    # Get all purchased products by the current user
    paid_products = current_user.purchased_products.filter_by(payment_status=True).all()

    return render_template(
        'dashboard_customer.html',
        title='Purchase History',
        paid_products=paid_products)


@app.route('/shop/product/<int:id>', methods=['GET', 'POST'])
def view_product(id):
    if current_user.is_authenticated:
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer'))
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
    product = ProductsForSale.query.filter_by(id=id).first_or_404()
    form = AddToCart()
    if form.validate_on_submit():
        if 'cart' in session:
            session['cart'] = []
            add_product = {"product_id": product.id,"quantity": form.quantity.data}
        session['cart'].append(add_product)
        return redirect(url_for('shop'))

    return render_template(
        'product_customer.html',
        title='Product Details',
        product=product,
        form=form)


@app.route('/customer/cart-items')
def dashboard_customer_cart_items():
    if current_user.is_authenticated:
        if current_user.type == 'customer':
            return redirect(url_for('dashboard_customer'))
        if current_user.type == 'admin':
            return redirect(url_for('dashboard_admin'))
    cart_items = PurchasedProducts.query.all()
    num_cart_items = len(cart_items)

    return render_template(
        'cart_items.html',
        title='Cart Items',
        cart_items=cart_items,
        num_cart_items=num_cart_items)


@app.route('/dashboard/customer/cart-item/<int:id>/delete')
@login_required
def dashboard_customer_cart_items_delete(id):
    cart_item = PurchasedProducts.query.filter_by(id=id).first_or_404()
    db.session.delete(cart_item)
    db.session.commit()
    flash(f'{cart_item.name} deleted from your cart.')
    return redirect(url_for('dashboard_customer_cart_items'))


@app.route('/dashboard/customer/cart-items/ready-to-buy')
@login_required
def dashboard_customer_checkout():
    cart_items = PurchasedProducts.query.all()
    num_cart_items = len(cart_items)

    return render_template(
        'cart_items_checkout.html',
        title='Buy Your Items',
        cart_items=cart_items,
        num_cart_items=num_cart_items)


@app.route('/dashboard/customer/cart-item/<int:id>/buy')
@login_required
def dashboard_customer_buy_product(id):
    cart_items = PurchasedProducts.query.all()
    for item in cart_items:
        if item.id is id:
            if item.customer_id is None:
                item.customer_id = current_user.id
                db.session.commit()
    return redirect(url_for('dashboard_customer_checkout'))


@app.route('/product/<int:id>/lipa-na-mpesa')
@login_required
def lipa_na_mpesa(id):    
    pass   
    return redirect(url_for('dashboard_customer'))

# ---------------------
# End: Dashboard customer
# ---------------------



# ---------------------
# Start: Dashboard admin
# ---------------------



# ---------------------
# Start: Dashboard admin
# ---------------------