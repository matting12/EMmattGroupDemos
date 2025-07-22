# todo_manager.py - Simple Todo List Manager
import json
from datetime import datetime

class TodoManager:
    def __init__(self):
        self.todos = []
        self.next_id = 1
    
    def add_todo(self, title, description=""):
        todo = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.next_id += 1
        return todo['id']
    
    def mark_completed(self, todo_id):
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().isoformat()
                return True
        return False
    
    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
    
    def get_todos(self, show_completed=True):
        if show_completed:
            return self.todos
        return [todo for todo in self.todos if not todo['completed']]
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.todos = json.load(f)
                if self.todos:
                    self.next_id = max(todo['id'] for todo in self.todos) + 1
        except FileNotFoundError:
            pass

# Example usage
if __name__ == "__main__":
    manager = TodoManager()
    
    # Add some todos
    manager.add_todo("Buy groceries", "Milk, eggs, bread")
    manager.add_todo("Finish project", "Complete the Python assignment")
    manager.add_todo("Call mom")
    
    # Mark one as completed
    manager.mark_completed(1)
    
    # Show all todos
    print("All todos:")
    for todo in manager.get_todos():
        status = "✓" if todo['completed'] else "○"
        print(f"{status} {todo['title']}: {todo['description']}")