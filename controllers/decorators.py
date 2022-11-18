from functools import wraps
from flask import flash, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Login Required!","secondary")
            return redirect(url_for('login'))
    return wrap