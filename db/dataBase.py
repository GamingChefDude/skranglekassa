import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="Products_db_skranglekassa",
        user="postgres",
        password=os.getenv("password")
    )

def fetch_all_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products;")
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products

def get_user_by_email(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user