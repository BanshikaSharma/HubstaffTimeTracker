from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample in-memory storage for todos
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    content = request.form['todo_content']
    todo_id = len(todos)  # Simple ID based on the current length of the list
    todos.append({'id': todo_id, 'content': content, 'date': datetime.now()})
    return redirect(url_for('index'))

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    todo_id = int(request.form['todo_id'])
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
