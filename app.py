import os
import psycopg2

def get_message():
    return "Hello, World!"

def check_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "testdb"),
        user=os.getenv("POSTGRES_USER", "testuser"),
        password=os.getenv("POSTGRES_PASSWORD", "testpassword"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port= int(os.getenv("POSTGRES_PORT", "5432"))
    )
    cur= conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] == 1

def add_integer(a, b):
    return a + b

if __name__ == "__main__":
    print(get_message())
    if check_db_connection():
        print("Database connection established")
