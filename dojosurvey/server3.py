from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret.key = 'paK4OM7R4c2Zz40XL27Id92TW53GhZx9'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=["POST"])
def results():
   return render_template("results.html", name = request.form['form_name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True)
