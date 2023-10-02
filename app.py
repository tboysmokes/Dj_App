from flask import Flask, render_template, url_for
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

def api_call():
    pass

if __name__ == ('__main__'):
    app.run(debug=True)