from flask import Flask, render_template, session, g, url_for, request
from login_utils import encrypt_password, check_password

app = Flask(__name__)

@app.route('/')
def index():
    context = {'page_title':'Home'}
    return render_template('index.html',**context)
@app.route('/blog')
def blog():
    context = {'page_title':'Our Blog',
               'home_link' : True}
    return render_template('index.html',**context)
@app.route('/about_us')
def about_us():
    context = {'page_title':'About Us',
               'home_link' : True}
    return render_template('index.html',**context)
@app.route('/contact_us')
def contact_us():
    context = {'page_title':'Contact Us',
               'home_link' : True}
    return render_template('index.html',**context)
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method.upper() == 'POST':
        context = {
            'var' : {
                'a':request.form['username'],
                'b':request.form['password']
                }
            }
        return render_template("test.html",**context)
    else:
        context = {
            'var' : request.remote_addr,
               'back_link' : True
        }        
        return render_template("login_form.html",**context)

@app.route('/logout')
def logout():
    pass

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method.upper() == 'POST':
        session.register = True
        username = request.form['username']
        pass_a = encrypt_password(request.form['password_1'])
        pass_b = request.form['password_2']
        if check_password(pass_b,pass_a):
            session.match = True
            context = {
                'var' : username,
                'home_link': session.match
            }
        else:
            context = {
                    'back_link':True
            }
        return render_template("test.html",**context)
    else:
        session.register = True
        context = {
            'var' : request.remote_addr,
            'home_link': True,
            }
    return render_template("login_form.html",**context)

if __name__ == "__main__":
    app.run()
