import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { TodoContext } from '../contexts/TodoContext';

function AddTodoForm() {
  const [title, setTitle] = useState('');
  const history = useHistory();
  const { addTodo } = useContext(TodoContext);

  // Функция для обработки отправки формы
  const handleSubmit = (e) => {
    e.preventDefault();

    // Добавление задачи с использованием контекста
    addTodo(title);

    // Перенаправление на главную страницу после добавления задачи
    history.push('/');
  };

  return (
    <div>
      <h2>Add Todo</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}

export default AddTodoForm;
