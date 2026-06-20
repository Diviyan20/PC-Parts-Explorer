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

def connection():
    conn = psycopg2.connect(
        database=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST, 
        port=5432
    )
    return conn

def test_fetch():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    record = cur.fetchall()

    print("Data: ", record)


def insert_user(username, email, full_name, password):
    conn = connection()
    cur = conn.cursor()

    query = "INSERT INTO users (username, email, full_name, password) VALUES (%s, %s, %s, %s)"

    try:
        cur.execute(query, (username, email, full_name, password))
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise ValueError("Database Error:", e)
    
    finally:
        cur.close()
        conn.close()

