"""
todo_manager.py - Todo List Manager

FUNCTIONALITY OVERVIEW:
This version attempts to enhance the original todo manager by adding a priority system:
- All original todo operations (add, complete, view, save/load)
- NEW: Priority levels (1=high, 2=medium, 3=low) for todos
- NEW: Sorting todos by priority level
- Enhanced todo management with priority-based organization

WHAT TO REVIEW:
- Is there any missing functionality?
- Broken logic?
- Readability
- Code structure and organization

"""
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
        except FileNotFoundError:
            pass
    
    # NEW: Added priority feature
    def set_priority(self, todo_id, priority):
        """Set priority for a todo item (1=high, 2=medium, 3=low)"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['priority'] = priority
                return True
        return False
    
    def get_todos_by_priority(self):
        """Get todos sorted by priority"""
        return sorted(self.todos, key=lambda x: x.get('priority', 3))

# Example usage
if __name__ == "__main__":
    manager = TodoManager()
    
    # Add some todos
    id1 = manager.add_todo("Buy groceries", "Milk, eggs, bread")
    id2 = manager.add_todo("Finish project", "Complete the Python assignment")
    
    # Set priorities
    manager.set_priority(id1, 2)  # medium priority
    manager.set_priority(id2, 1)  # high priority
    
    # Show todos by priority
    for todo in manager.get_todos_by_priority():
        priority_text = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}.get(todo.get('priority', 3), "UNKNOWN")
        print(f"[{priority_text}] {todo['title']}: {todo['description']}")