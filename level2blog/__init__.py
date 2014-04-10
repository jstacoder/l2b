#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#

import os
from functools import wraps
from flask import (Flask, flash, redirect, url_for, request, session, g,
render_template )
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import LoginForm, RegisterForm, ForgotForm
from register import register_user
from login_utils import encrypt_password
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


# Login required decorator.
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html')

@login_required
@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        session['logged_in'] = True
        flash('Thanks for logging in {}'.format(request.form['name']))
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    return render_template('forms/login.html',form=form,error=error)

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        user, email, pw1, pw2 = request.form['name'],request.form['email'],request.form['password'],request.form['confirm']
        if not pw1 == pw2:
            flash("Passwords dont match, try again")
            return redirect(url_for('register'))
        else:
            newUser = register_user(user,encrypt_password(pw1),email)
            flash('Hi '+str(newUser)+', thank you for registering')
            flash('Your email address is: '+newUser.get_email())
            return redirect(url_for('home'))
    form = RegisterForm(request.form)
    return render_template('forms/register.html',form=form)

@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html',form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You logged out, goodbye')
    return redirect(url_for('home'))

@app.route('/blog')
def blog():
    pass



# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
#if __name__ == '__main__':
#    app.run()

# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

