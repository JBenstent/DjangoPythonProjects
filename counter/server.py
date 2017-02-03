from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'f;ijas;lkahdrahsdf'

@app.route('/')
def index():
    if 'counter' in session:
      session['counter'] += 1
    else:
      session['counter'] = 1
    return render_template("index.html")

@app.route('/1')
def add2():
    session['counter'] += 1
    return redirect('/')

@app.route('/2')
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
