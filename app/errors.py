from app import db, app
from flask import render_template


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('errors/500.html', title="Unexpected Internal Error"), 500
