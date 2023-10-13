from flask import Flask, render_template, url_for, request, redirect
import api
import sqlite3
import requests

global userid
userid = 1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feeltherythm'

connection = sqlite3.connect("user.db", check_same_thread=False)
cursor = connection.cursor()


query = '''
CREATE TABLE IF NOT EXISTS users(
    user_id    INTEGER   PRIMARY KEY,
    username   TEXT      NOT NULL,
    email      TEXT      NOT NULL UNIQUE,
    age        INTEGER   NOT NULL,
    password   TEXT      NOT NULL
    )
'''

query2 = '''
CREATE TABLE IF NOT EXISTS userParameters(
    userid    INTEGER,
    Genre     TEXT   NOT NULL,
    FOREIGN KEY (userid) REFERENCES users(user_id)
    )
'''

query3 = '''
CREATE TABLE IF NOT EXISTS userMusic(
   userid          INTEGER,
   Music           TEXT  NOT NULL,
   MusicGenre      TEXT  NOT NULL,
   
   FOREIGN KEY (userid) REFERENCES users(user_id)
   )
'''

cursor.execute(query)
cursor.execute(query2)
cursor.execute(query3)




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
            return redirect("/home", code= 302)
        
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
    if request.method == "POST":
        artist = request.form['']

    token = api.get_token()
    artist_id = api.search_for_artist(token, artist)
    artist_track = api.get_artist_song(token, artist_id)
    return render_template('home.html')


if __name__ == ('__main__'):
    app.run(debug=True)