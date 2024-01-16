# Shop Online (For Glasses)

### Steps followed when converting the original static web website to Flask:

**These have already been done for you; just a note here**.

1. Create a scalable Flask project structure:

```
shoponline_folder
    | --- main.py
    | --- config.py
    | --- .flaskenv
    | --- .env
    | --- requirements.txt
    | --- README.md
    | --- .gitignore
    | --- app/
           | --- __init__.py
           | --- routes.py
           | --- forms.py
           | --- models.py
           | --- email.py
           | --- templates/
                    | --- base.html
           | --- static
                   | --- css/
                          | --- custom.css
                   | --- images/
                   | --- js
```

2. Create and activate a virtual environment as follows:

    ```python
    $ python3 -m venv shoponline_venv         # create a virtualenv called shoponline_venv
    $ source shoponline_venv/bin/activate     # activate the virtualenv

    # Outcome
    (shoponline_venv)$
    ```

3. Install needed packages:

    - Flask microframework
    - Flask-Login to handle user sessions
    - Flask-sqlalchemy: a Flask-friendly ORM
    - Flask-migrate: Migration management
    - Python-dotenv: Load environment variables
    - PyJWT: working with JSON
    - Email-validator: used when emails are incorporated in Flask web forms
    - Flask-wtf: working with web forms

    ```python
    # How installation was done
    (shoponline_venv)$ pi3 install flask flask-login flask-sqlalchemy ...
    ```

4. Create an application instance as seen in `app/__init__.py`
5. Return random string such as 'hello world' as seen in `app/routes.py`
6. Create an entry point to the application as seen in `main.py`
7. Instantiate needed Flask environment variables as seen in `.flaskenv`
8. Update the `requirements.txt` file by running this command in the terminal:

    ```python
    (shoponline_venv)$ pip3 freeze > requirements.txt
    ```
9. Start the Flask server by running this in an active virtualenv:
    ```python
    (shoponline_venv)$ flask run

    # Your server should start
    ```

## Using The Flask Side Of The Project

1. Merge the changese between the forks

2. In your terminal, update your local repo with the changes seen in the PR:

    ```python
    $ git pull origin main
    ```

3. Activate the virtualenv called **shoponline_venv**:

    ```python
    $ source shoponline_venv/bin/activate

    # Your terminal will change to:
    (shoponline_venv)$
    ```

4. Install all project dependancies in your active virtualenv:

    ```python
    (shoponline_venv)$ pip3 install -r requirements.txt
    ```

5. Create and update a `.env` file in the root directory:

    ```python

    # This creates a .env file with the environment variables seen in .env-template file
    (shoponline_venv)$ cp .env-template .env

    # Update values in the .env file
    # For example:
    # Run this in your terminal:
    # python3 -c 'import secrets; print(secrets.token_hex(16))'
    # Copy and paste the value in .env's SECRET_KEY
    ```

6. Start your Flask server:

    ```python
    (shoponline_venv)$ flask run
    ```

7. Copy and paste this link in a web browser

    ```python
    http://127.0.0.1:5000

    # This link is available in your terminal
    ```


# Technologies Used

- Flask microframework
- Daraja API for MPesa
- Stripe
- Flask login to manage user authentication
- Flask migrate to handle database migration
- Flask SQLAlchemy for database management
- Twilio Sendgrid
- Twilio Verify

# Features

- User authentication
- Add product(s) to cart
- MPesa/Card payment
- User verification using email address
- Two-factor authentication using Phone number
- Error handling


# Additional Information

| Database Design | UI Design | Live Link |
| --------------- | --------- | --------- |
| [DrawSQL](https://drawsql.app/teams/gitau-harrison/diagrams/sample-ecommerce-app) | [Figma]() | [Render]() |