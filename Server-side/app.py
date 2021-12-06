from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome to my website!'

@app.route('/about')
def about():
    return 'Welcome About page :) '

@app.route('/page')
def page():
 return redirect('/')

@app.route('/anotherPage')
def anotherPage():
 return redirect(url_for('about'))


if __name__ == '__main__':
    app.run()