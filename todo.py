from flask import Flask, render_template, request

app=Flask(__name__)

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
def add():
    new_todo= request.form('new_todo')
    new_todo=input('What do you want to do before year ends?')
    return new_todo



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

cursor=connection.cursor()

cursor.execute('SELECT * FROM `todos`')

result=cursor.fetchall()

print(result[1]['Description'])