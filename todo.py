from flask import Flask, render_template, request

app=Flask(__name__)

my_todos=[
    'Grow a couple more inches',
    'Get scholarships for track'
]

@app.route('/')
def index():
    return render_template(
        'todo.html.jinja',
        todos=my_todos
     )

@app.route('/add', methods=['POST'])
def add():
    new_todo= request.form('new_todo')
    return new_todo