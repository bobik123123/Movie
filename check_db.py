import psycopg2
import os

dsn = os.getenv('DATABASE_URL', "postgres://movie_admin:movie_admin@movie_db:5432/movie_db")
connection = None

try:
    connection = psycopg2.connect(dsn)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to PostgreSQL database, version: {db_version}")

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
