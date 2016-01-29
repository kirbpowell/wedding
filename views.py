from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Patton and Kirby\'s Wedding Website!',
                           welcome='Welcome to our wedding website.',
                           info='''The final version of our wedding website is
still under construction, but feel free to check back often for Wedding,
Travel and Reception updates!''')
