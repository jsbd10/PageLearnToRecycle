from flask import Flask
from flask import render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')


@app.route('/recicla')
def recicla():
    return render_template('recicla.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
