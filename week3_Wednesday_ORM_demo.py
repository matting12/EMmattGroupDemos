from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.secret_key = 'your-secret-key-here-change-in-production'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


with app.app_context():
    db.create_all()

    sample_users = [
        User("Alice", "alice@example.com"),
        User("Charlie", "charlie@example.com"),
        User("Bob", "bob@example.com"),
    ]
    
    for user in sample_users:
        user.save()



@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Add new user to list
        user = User(name, email)
        user.save()
        
        # Flash a success message
        flash(f'User {name} registered successfully!', 'success')
        
        # Redirect to home page
        return redirect(url_for('home'))
    
    # GET request - show the form
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)