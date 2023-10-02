from flask import Flask, render_template, url_for, request, redirect
from dotenv import load_dotenv
import sqlite3
import requests
import os

load_dotenv()

connection = sqlite3.connect("userdatabase.db", check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feeltherythm'

query = '''
CREATE TABLE IF NOT EXISTS users(
    user_id   INTEGER   PRIMARY KEY
    username   TEXT      NOT NULL,
    email      TEXT      NOT NULL UNIQUE,
    age       INTEGER    NOT NULL,
    password   TEXT      NOT NULL
    )
'''

cursor.execute(query)


app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "PSOT":
        email = request.form['']
        password = request.form['']

        query = ("SELECT * FORM users WHERE email = '"+email+"' AND  password = '"+password+"' ")
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            print("unknown users")
        else:
            return redirect("/home", code = 302)
        
    return render_template('login.html')
                 


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['']
        email = request.form['']
        age = request.form['']
        password = request.form['']

        cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)",userid , username, email, age, password)
        connection.commit()

        return login()
    return render_template("signup.html")


@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])
def home():
    pass


def api_call():
    pass

if __name__ == ('__main__'):
    app.run(debug=True)