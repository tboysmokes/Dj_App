from flask import Flask, render_template, url_for, request, redirect


global userid
userid = 1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feeltherythm'


@app.route('/', methods= ['GET', 'POST'])
@app.route('/home', methods= ['GET', 'POST'])
def home():
    if request.method == "POST":
        artist = request.form['']
    return render_template('home.html')


if __name__ == ('__main__'):
    app.run(debug=True)