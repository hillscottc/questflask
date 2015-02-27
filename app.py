import os
from flask import Flask, request, session, g, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

import models

@app.before_request
def before_request():
    g.db = db
    g.app = app

# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    


@app.route('/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)


@app.route('/clues/')
def show_entries():
    cur = g.db.execute('select category, question, answer from questapp_clue')
    clues = [dict(category=row[0], question=row[1], answer=row[2]) for row in cur.fetchall()]
    return render_template('clues.html', clues=clues)

# @app.route("/")
# def show(id):
#     pastes = models.Paste.query.filter_by(id=id)
#     paste = pastes.first()

#     if paste == None:
#         raise Exception("No such paste by id %s" % id)

#     return render_template("paste.html", paste=paste)



    


if __name__ == '__main__':
    app.run(debug=True)