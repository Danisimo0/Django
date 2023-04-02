from flask import Flask, request
import psycopg2

app = Flask(__name__)


# думал сначала сюда записать 1 базу, а потом ее цеплять ко всем функциям,
# потом понял что лучше к каждой функции подключать разные
# так как под каждую задачу (Todo_crud) может быть разная база данных что бы не нагружать 1 или
# я не правильно понял и можно было подключить 1 базу и от нее цепляться к примеру:


# connection = psycopg2.connect(database=///, user=///, password=///, host=///, port=///)
# cursor =  connection.cursor()


# @app.route('/new', methods=['POST'])
# def create_todo():
#     cursor.execute(///)


#     connection.commit() /TODO


# @app.route('/update/<int:id>', methods=['POST'])
# def update(id):

#     cursor.execute(///)


#    connection.commit() /TODO


@app.route("/todos", methods=['GET'])
def todos():
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos;")
    rows = cursor.fetchall()
    objs = [
        {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
        for row in rows
    ]
    return objs


@app.route("/todos/<todo_id>", methods=['GET'])
def todos_id(todo_id):
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    #   cursor.execute("SELECT * FROM todos ORDER BY id")
    cursor.execute(f"select id, title, description, date_create, status from todos where id='{todo_id}';")
    row = cursor.fetchone()
    obj = {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
    return obj


@app.route("/todos/create", methods=['GET', 'POST'])
def todos_create(todo_id):
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute(f"select id, title, description, date_create, status from todos where id='{todo_id}';")
    row = cursor.fetchone()
    obj = {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
    return obj


@app.route("/todos/delete", methods=['POST'])
def todos_delete(todo_id):
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM todos WHERE id='{todo_id}';")
    row = cursor.fetchone()
    obj = {"id": row[0]}
    return obj


if __name__ == '__main__':
    app.run(debug=True)
