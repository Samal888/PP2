import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="Salamat6!",
    host="localhost",
    port="5432"
)

print("Connected!")

conn.close()