from flask import Flask, render_template, url_for
app = Flask(__name__)

ACTIVE_STATE = ['active', '', '', '', '']
WEDDING_PARTY = [["Adam Powell", "Annie Dore"],
                 ["Kyle Gibbons", "Evva Frisby"],
                 ["Mark Baumann", "Meggan Wolanin"],
                 ["Wes Winn", "Victoria Peckham"]]
RECEPTION_INFO = """The reception will follow the ceremony. We've got quite
a bit planned, and we think it's going to be a great time. We're still
hammering out the details though, so further information will be forthcoming
 with your invitation."""
BOND = """Located just off of the University of Chicago's main quad is
the Joseph Bond Chapel, the beautiful and intimate Gothic Revival setting for
our wedding. Built in 1926, the chapel features the stunning Reneker Organ,
fantastic stained glass windows, as well as truly inspiring
architecture and inscriptions. We think that it is going to be the perfect
place to take our first steps into marriage together, and we hope you'll be
able to join us."""


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
    return render_template('dayof.html',
                           active_state=ACTIVE_STATE,
                           img=url_for('static',
                                       filename="img/bond.jpg"),
                           alttext="Bond Chapel",
                           bondBlurb=BOND,
                           reception=RECEPTION_INFO)


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
