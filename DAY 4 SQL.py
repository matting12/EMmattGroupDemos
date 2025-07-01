import sqlite3

def print_table(table_name):
    """Helper function to print table contents in a nice format"""
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    
    print(f"\nTable: {table_name}")
    print("-" * 50)
    
    # Print header
    header = " | ".join(f"{col:15}" for col in columns)
    print(header)
    print("-" * len(header))
    
    # Print rows
    if rows:
        for row in rows:
            row_str = " | ".join(f"{str(val):15}" for val in row)
            print(row_str)
    else:
        print("(empty table)")
    print()


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        budget INTEGER
    )
''')
print("[OK] Created departments table")
print_table("departments")

cursor.execute("INSERT INTO departments (name, budget) VALUES ('Engineering', 500000)")
cursor.execute("INSERT INTO departments (name, budget) VALUES ('Marketing', 200000)")
cursor.execute("INSERT INTO departments (name, budget) VALUES ('Sales', 300000)")
print("[OK] Inserted 3 departments")
print_table("departments")


# Employees table (child with foreign key)
cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary INTEGER,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
''')
print("[OK] Created employees table (with foreign key to departments)")
print_table("employees")

employees_data = [
    ('Alice Johnson', 75000, 1),
    ('Bob Smith', 65000, 1),
    ('Carol White', 55000, 2),
    ('David Brown', 70000, 2),
    ('Eve Davis', 80000, 3)
]

cursor.executemany(
    "INSERT INTO employees (name, salary, department_id) VALUES (?, ?, ?)",
    employees_data
)
print("[OK] Batch inserted 5 employees")
print_table("employees")

# INNER JOIN
print("INNER JOIN - Employees with their departments:")
cursor.execute('''
    SELECT e.name, e.salary, d.name as department
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id
    ORDER BY d.name, e.salary DESC
''')
for row in cursor.fetchall():
    print(f"  {row[0]} (${row[1]:,}) - {row[2]}")