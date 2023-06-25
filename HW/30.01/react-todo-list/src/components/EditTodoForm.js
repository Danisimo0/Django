import React, { useState, useContext } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { TodoContext } from '../contexts/TodoContext';

function EditTodoForm() {
  const { id } = useParams();
  const [title, setTitle] = useState('');
  const history = useHistory();
  const { todos, updateTodo } = useContext(TodoContext);

  // Найдите задачу по id и установите начальное значение для поля `title`
  const selectedTodo = todos.find((todo) => todo.id === parseInt(id));
  if (selectedTodo) {
    setTitle(selectedTodo.title);
  }

  // Функция для обработки отправки формы
  const handleSubmit = (e) => {
    e.preventDefault();

    // Обновление задачи с использованием контекста
    const updatedTodo = { ...selectedTodo, title: title };
    updateTodo(selectedTodo.id, updatedTodo);

    // Перенаправление на главную страницу после обновления задачи
    history.push('/');
  };

  return (
    <div>
      <h2>Edit Todo</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button type="submit">Update</button>
      </form>
    </div>
  );
}

export default EditTodoForm;
