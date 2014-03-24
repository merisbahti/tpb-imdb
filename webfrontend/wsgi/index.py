import os
from flask import Flask
from flask import request
from flask import render_template
import sqlite3
import re


app = Flask(__name__, static_folder='static', static_url_path='')
app.config['DEBUG'] = True

@app.route("/")
def index():
    # If on local
    #conn = sqlite3.connect("wsgi/db.db")
    # If on server
    conn = sqlite3.connect("/var/lib/openshift/53307bdde0b8cdb76f000247/app-root/runtime/repo/wsgi/db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    conn.close()
    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run()
