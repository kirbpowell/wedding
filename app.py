from flask import Flask, render_template, url_for
import constants as const
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    const.ACTIVE_STATE = ['active', '', '', '', '']
    return render_template('index.html.j2',
                           title=const.TITLE,
                           welcome=const.WELCOME,
                           # info=THE_INFO,
                           img=url_for('static', filename=const.HOME_IMG),
                           alt=const.HOME_ALTTEXT,
                           active_state=const.ACTIVE_STATE)


@app.route('/ourStory')
def ourStory():
    const.ACTIVE_STATE = ['', 'active', '', '', '']
    return render_template('content.html.j2',
                           active_state=const.ACTIVE_STATE)


@app.route('/dayOf')
def dayof():
    const.ACTIVE_STATE = ['', '', 'active', '', '']
    return render_template('dayof.html.j2',
                           active_state=const.ACTIVE_STATE,
                           img=url_for('static', filename=const.BOND_IMG),
                           alttext=const.BOND_ALTTEXT,
                           bondBlurb=const.BOND,
                           reception=const.RECEPTION_INFO)


@app.route('/weddingParty')
def party():
    const.ACTIVE_STATE = ['', '', '', 'active', '']
    return render_template('wedding_party.html.j2',
                           wedding_party=const.WEDDING_PARTY,
                           active_state=const.ACTIVE_STATE)
    # return render_template('content.html.j2',
    #                        active_state=const.ACTIVE_STATE)


@app.route('/registries')
def gifts():
    const.ACTIVE_STATE = ['', '', '', '', 'active']
    return render_template('content.html.j2',
                           active_state=const.ACTIVE_STATE)


if __name__ == '__main__':
    app.run(debug=True)
