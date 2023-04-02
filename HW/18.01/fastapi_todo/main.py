from fastapi import FastAPI, HTTPException
from typing import List, Union
import psycopg2

app = FastAPI()






class TodoModel:
    def __init__(self, id: int, title: str, completed: bool):
        self.id = id
        self.title = title
        self.completed = completed


# тип данных для входных параметров
TodoInput = Union[str, bool]


# создание todo
@app.post("/todos/")
async def create_todo(
    title: str,
    completed: bool = False
) -> TodoModel:
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO todos (title, completed)
        VALUES (%s, %s)
        RETURNING id, title, completed;
    """, (title, completed))


    todo = cursor.fetchone()
    return TodoModel(todo[0], todo[1], todo[2])


# получение всех todos
@app.get("/todos/", response_model=List[TodoModel])
async def get_todos() -> List[TodoModel]:
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, title, completed FROM todos;
    """)
    todos = []
    for todo in cursor.fetchall():
        todos.append(TodoModel(todo[0], todo[1], todo[2]))
    return todos


# получение todo по id
@app.get("/todos/{todo_id}", response_model=TodoModel)
async def get_todo_by_id(todo_id: int) -> TodoModel:
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, title, completed FROM todos WHERE id='{todo_id}';)
    """, (todo_id,))
    todo = cursor.fetchone()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoModel(todo[0], todo[1], todo[2])


# обновление todo
@app.put("/todos/{todo_id}", response_model=TodoModel)
async def update_todo(
    todo_id: int,
    title: TodoInput = None,
    completed: TodoInput = None
) -> TodoModel:
    # получение todo по id
    connection = psycopg2.connect(
        user="todolist_usr",
        password="Gosamu11",
        host="127.0.0.1",
        port="5432",
        dbname="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, title, completed FROM todos WHERE id='{todo_id}';
    """, (todo_id,))
    todo = cursor.fetchone()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # обновление todo
    if title is not None:
        connection = psycopg2.connect(
            user="todolist_usr",
            password="Gosamu11",
            host="127.0.0.1",
            port="5432",
            dbname="postgres",
        )
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE todos SET title='{todo_id}';
            """)