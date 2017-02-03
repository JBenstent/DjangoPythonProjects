from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    if 'hiddenNum' not in session:
        session['hiddenNum'] = random.randrange(1,4)
        print session['hiddenNum']
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['inputNum'] = int(request.form['number'])
    print "test for process"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print "test for reset"
    for key in session.keys():
        session.pop(key)
    print session
    return redirect('/')

app.run(debug=True)
