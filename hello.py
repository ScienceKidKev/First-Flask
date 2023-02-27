from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html.jinja', 
                           my_variable='wagwan', 
                           my_list=['dogs','cats','rabbits'])

@app.route('/ping')
def ping():
    return'<p>pong</p>'

@app.route('/hello/<name>')
def hello(name):
    return f'<p>Hello, {name}!</p>'