from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feeltherythm'

if __name__ == ('__main__'):
    app.run(debug=True)