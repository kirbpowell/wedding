from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Patton and Kirby\'s Wedding Website!',
                           welcome='Welcome to our wedding website.',
                           info='''The final version of our wedding website is
still under construction, but feel free to check back often for Wedding,
Travel and Reception updates!''',
                           img=url_for('static',
                                       filename="img/vienna.jpg"),
                           alt="Patton and Kirby together!")


@app.route('/ourStory')
def ourStory():
    return render_template('content.html',
                           some_content="Our story will go here.")


@app.route('/weddingParty')
def party():
    return render_template('content.html',
                           some_content="Info about the wedding party.")


@app.route('/gifts')
def gifts():
    return render_template('content.html',
                           some_content="Info about gift registries etc.")


@app.route('/dayOf')
def dayof():
    return render_template('content.html',
                           some_content="Details on the day of.")


if __name__ == '__main__':
    app.run(debug=True)
