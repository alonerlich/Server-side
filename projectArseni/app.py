from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

@app.route("/about")
def about():
    return redirect(url_for("CV"))

@app.route("/")
def CV():
    return render_template('CVgrid.html')

@app.route("/exercise2")
def exercise2():
    return render_template('exercise2.html')

@app.route("/form")
def form():
    return render_template('forms.html')

@app.route("/mistake")
def mistake():
    return redirect('/')

@app.route("/assignment8")
def assignment8():
    hobbies = {"soccer", "arsenal", "climbing", "web!!!!!!!", "surfing", "cooking"}
    return render_template('assignment8.html',hobbies = hobbies )

if __name__=="__main__":
    app.run()