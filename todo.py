from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Kevaughn": generate_password_hash("wagwan"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


my_todos=[
    'Grow a couple more inches',
    'Get scholarships for track'
]




@app.route('/')
def index():
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `todos`')

    results=cursor.fetchall()
     
    return render_template(
        'todo.html.jinja',
        todos=results
     )

@app.route('/add', methods=['POST'])
@auth.login_required
def add():
    new_todo = request.form['new_todo']
    cursor=connection.cursor()
    cursor.execute(f"INSERT INTO `todos`(`Description`) VALUES ('{new_todo}') ")
    my_todos.append(new_todo)
    return redirect('/')
    


@app.route('/complete', methods=['POST'])
@auth.login_required
def complete():
        todo_id = request.form['todo_id']

        cursor=connection.cursor()

        cursor.execute(f'UPDATE `todos` SET `Complete` = 1 WHERE `ID` = {todo_id}')


        return redirect('/')




import pymysql
import pymysql.cursors

connection= pymysql.connect(
    host='10.100.33.60',
    user='kheron',
    password='222755613',
    database='kheron_todo',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)







