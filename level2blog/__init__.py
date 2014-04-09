from flask import Flask, render_template, session, g, url_for

app = Flask(__name__)

@app.route('/')
def index():
    context = {'page_title':'Home'}
    return render_template('index.html',**context)
@app.route('/blog')
def blog():
    context = {'page_title':'Our Blog'}
    return render_template('index.html',**context)
@app.route('/about_us')
def about_us():
    context = {'page_title':'About Us'}
    return render_template('index.html',**context)
@app.route('/contact_us')
def contact_us():
    context = {'page_title':'Contact Us'}
    return render_template('index.html',**context)




if __name__ == "__main__":
    app.run()
