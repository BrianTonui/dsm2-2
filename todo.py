# todo.py

import os
import json

TODO_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []

    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def add_todo(todo):
    todos = load_todos()
    todos.append({"task": todo, "completed": False})
    save_todos(todos)

def list_todos():
    todos = load_todos()
    if not todos:
        print("No to-dos found.")
        return

    for i, todo in enumerate(todos, start=1):
        status = "✓" if todo["completed"] else "✗"
        print(f"{i}. [{status}] {todo['task']}")

def complete_todo(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid index.")
        return

    todos[index - 1]["completed"] = True
    save_todos(todos)
