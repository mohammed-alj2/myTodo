from flask import render_template, session, redirect


def error(error_code, message):
    return render_template('error.html', error_code=error_code, message=message)


def login_required(f):
    def wrapper(*args, **kwargs):
        if session['user_id']:
            return f(*args, **kwargs)
        return redirect('/login')
    return wrapper