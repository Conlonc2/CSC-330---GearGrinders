from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landingPage.html')


@app.route('/login')
def login():
    return render_template('login.html')


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8080, debug=True)
