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
    new_todo = request.form['new_todo']
    cursor=connection.cursor
    cursor.execute(f"INSERT INTO `todos`(`Description`) VALUES ('{new_todo}') ")
    my_todos.append(new_todo)
    return result(('/todo'))
    


@app.route('/complete', methods=['POST'])
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









