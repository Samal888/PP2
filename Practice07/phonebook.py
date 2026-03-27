import psycopg2
import csv
import config

# подключение к PostgreSQL
conn = psycopg2.connect(
    dbname=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT
)

cur = conn.cursor()

print("1 - Add (console)")
print("2 - Add (CSV)")
print("3 - Show")
print("4 - Update")
print("5 - Delete")

choice = input("Choose: ")

# 1. Добавить через консоль
if choice == "1":
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added!")

# 2. Добавить из CSV
elif choice == "2":
    with open("contacts.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV added!")

# 3. Показать все
elif choice == "3":
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

# 4. Обновить
elif choice == "4":
    name = input("Enter name: ")
    new_phone = input("New phone: ")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated!")

# 5. Удалить
elif choice == "5":
    name = input("Enter name: ")

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s",
        (name,)
    )
    conn.commit()
    print("Deleted!")

else:
    print("Wrong choice")

conn.close()