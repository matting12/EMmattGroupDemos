from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)

# Secret key for session management and security
# In production, use environment variable: app.secret_key = os.environ.get('SECRET_KEY')
app.secret_key = 'your-secret-key-here-change-in-production'

# Simple in-memory user storage (resets when server restarts)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

@app.route('/')
def home():
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Add new user to list
        new_id = len(users) + 1
        users.append({"id": new_id, "name": name, "email": email})
        
        # Flash a success message
        flash(f'User {name} registered successfully!', 'success')
        
        # Redirect to home page
        return redirect(url_for('home'))
    
    # GET request - show the form
    return render_template('register-template.html')

if __name__ == '__main__':
    app.run(debug=True)