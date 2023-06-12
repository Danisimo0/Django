import React, { useState } from 'react';
import { connect } from 'react-redux';
import { addTodo, toggleTodo, deleteTodo } from './redux/actions';

const App = ({ todos, addTodo, toggleTodo, deleteTodo }) => {
  const [text, setText] = useState('');

  const handleAddTodo = () => {
    if (text.trim() !== '') {
      addTodo(text);
      setText('');
    }
  };

  const handleToggleTodo = (id) => {
    toggleTodo(id);
  };

  const handleDeleteTodo = (id) => {
    deleteTodo(id);
  };

  return (
    <div>
      <h1>Todo List</h1>
      <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleAddTodo}>Add</button>
      <ul>
        {todos.map((todo) => (
          <li
            key={todo.id}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
            onClick={() => handleToggleTodo(todo.id)}
          >
            {todo.text}
            <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

const mapStateToProps = (state) => ({
  todos: state.todos,
});

const mapDispatchToProps = {
  addTodo,
  toggleTodo,
  deleteTodo,
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
