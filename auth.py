from db import get_connection

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print("Signup successful!")
    except:
        print("Username already exists.")
    finally:
        conn.close()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cur.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials")
        return False
