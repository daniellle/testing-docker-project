# web/app.py
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection settings from environment variables
db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")

@app.route("/")
def index():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            dbname=db_name
        )
        conn.close()
        return "Connected to the database successfully!"
    except Exception as e:
        return f"Failed to connect to the database: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
