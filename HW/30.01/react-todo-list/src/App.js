import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import TodoList from './components/TodoList';
import AddTodoForm from './components/AddTodoForm';
import EditTodoForm from './components/EditTodoForm';
import { TodoProvider } from './contexts/TodoContext';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="container">
          <Switch>
            <Route exact path="/" component={TodoList} />
            <Route path="/add" component={AddTodoForm} />
            <Route path="/edit/:id" component={EditTodoForm} />
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
