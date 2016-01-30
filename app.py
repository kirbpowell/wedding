from flask import Flask, render_template, url_for
app = Flask(__name__)

ACTIVE_STATE = ['active', '', '', '', '']
WEDDING_PARTY = [["Adam Powell", "Annie Dore"],
                 ["Kyle Gibbons", "Evva Frisby"],
                 ["Mark Baumann", "Meggan Wolanin"],
                 ["Wes Winn", "Victoria Peckham"]]


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
                           alt="Patton and Kirby together!",
                           active_state=ACTIVE_STATE)


@app.route('/ourStory')
def ourStory():
    ACTIVE_STATE = ['', 'active', '', '', '']
    return render_template('content.html',
                           some_content="Our story will go here.",
                           active_state=ACTIVE_STATE)


@app.route('/weddingParty')
def party():
    ACTIVE_STATE = ['', '', 'active', '', '']
    return render_template('wedding_party.html',
                           the_party=WEDDING_PARTY,
                           active_state=ACTIVE_STATE)


@app.route('/gifts')
def gifts():
    ACTIVE_STATE = ['', '', '', 'active', '']
    return render_template('content.html',
                           some_content="Info about gift registries etc.",
                           active_state=ACTIVE_STATE)


@app.route('/dayOf')
def dayof():
    ACTIVE_STATE = ['', '', '', '', 'active']
    return render_template('content.html',
                           some_content="Details on the day of.",
                           active_state=ACTIVE_STATE)


if __name__ == '__main__':
    app.run(debug=True)
