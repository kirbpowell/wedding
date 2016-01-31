from flask import Flask, render_template, url_for
app = Flask(__name__)

ACTIVE_STATE = ['active', '', '', '', '']
WEDDING_PARTY = [["Adam Powell", "Annie Dore"],
                 ["Kyle Gibbons", "Evva Frisby"],
                 ["Mark Baumann", "Meggan Wolanin"],
                 ["Wes Winn", "Victoria Peckham"]]
# THE_INFO = ''''''


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Patton and Kirby\'s Wedding Website!',
                           welcome='Welcome to our wedding website.',
                           # info=THE_INFO,
                           img=url_for('static',
                                       filename="img/vienna.jpg"),
                           alt="Patton and Kirby together!",
                           active_state=ACTIVE_STATE)


@app.route('/ourStory')
def ourStory():
    ACTIVE_STATE = ['', 'active', '', '', '']
    return render_template('content.html',
                           active_state=ACTIVE_STATE)


@app.route('/dayOf')
def dayof():
    ACTIVE_STATE = ['', '', 'active', '', '']
    return render_template('content.html',
                           active_state=ACTIVE_STATE)


@app.route('/weddingParty')
def party():
    ACTIVE_STATE = ['', '', '', 'active', '']
    # return render_template('wedding_party.html',
    #                        the_party=WEDDING_PARTY,
    #                        active_state=ACTIVE_STATE)
    return render_template('content.html',
                           active_state=ACTIVE_STATE)


@app.route('/registries')
def gifts():
    ACTIVE_STATE = ['', '', '', '', 'active']
    return render_template('content.html',
                           active_state=ACTIVE_STATE)


if __name__ == '__main__':
    app.run(debug=True)
