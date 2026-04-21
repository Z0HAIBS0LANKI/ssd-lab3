import sqlite3

# Hardcoded credentials (Security Issue #1)
DB_USER = "admin"
DB_PASS = "admin123"

def get_db():
    conn = sqlite3.connect('users.db')
    return conn

# No input validation (Security Issue #2)
def login(username, password):
    conn = get_db()
    
    # SQL Injection risk (Security Issue #3)
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    result = conn.execute(query).fetchone()
    return result

# Unsafe query construction (Security Issue #4)
def get_user_data(user_id):
    conn = get_db()
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchall()
