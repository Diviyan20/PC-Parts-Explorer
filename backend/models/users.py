import psycopg2
import os
from dotenv import load_dotenv

# ======================
# ENVIRONMENT VARIABLES 
# ======================
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def connection():
    conn = psycopg2.connect(
        database=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST, 
        port=DB_PORT
    )
    return conn

def test_fetch():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    record = cur.fetchall()

    print("Data: ", record)

# Registers a new user into the database
def insert_user(username, email, full_name, password):
    conn = connection()
    cur = conn.cursor()

    # SQL Query
    query = "INSERT INTO users (username, email, full_name, password) VALUES (%s, %s, %s, %s)"

    try:
        """
        - Cursor runs the query
        - The credentials are written and saved into the database
        """
        cur.execute(query, (username, email, full_name, password))
        conn.commit()

    # Rolls back the commit if there is an error
    except Exception as e:
        conn.rollback()
        raise ValueError("Database Error:", e)
    
    # Both connection and cursor should be closed to avoid leaks
    finally:
        cur.close()
        conn.close()

# Deletes a user from the database
def delete_user(username, password):
    conn = connection()
    cur = conn.cursor()

    query = "DELETE FROM users WHERE username = %s AND password = %s"

    try:
        cur.execute(query, (username, password))
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        raise ValueError("Database Error:", e)
    
    finally:
        conn.close()
        cur.close()