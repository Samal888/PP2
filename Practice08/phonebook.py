from connect import get_connection

def main():
    conn = get_connection()
    if not conn:
        print("Ошибка подключения!")
        return

    cur = conn.cursor()

    while True:
        print("\n=== Телефонная книга ===")
        print("1. Добавить/обновить контакт")
        print("2. Добавить несколько контактов")
        print("3. Поиск контакта")
        print("4. Показать контакты с пагинацией")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
            print(f"Контакт {name} добавлен/обновлён!")

        elif choice == "2":
            n = int(input("Сколько контактов добавить? "))
            names = []
            phones = []
            for i in range(n):
                nm = input(f"Имя {i+1}: ")
                ph = input(f"Телефон {i+1}: ")
                names.append(nm)
                phones.append(ph)
            cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))

        elif choice == "3":
            letter = input("Введите первую букву имени: ")
            cur.execute("SELECT name, phone FROM contacts WHERE name ILIKE %s;", (letter + '%',))
            for row in cur.fetchall():
              print(row)

        elif choice == "4":
            limit = int(input("Сколько записей вывести: "))
            offset = int(input("С какой записи начать: "))
            cur.execute("SELECT * from get_contacts_paginated(%s, %s);", (limit, offset))
            rows=cur.fetchall()
            for row in rows:
                print(row)

        elif choice == "5":
            del_id = input("Введите имя или телефон для удаления: ")
            cur.execute("CALL delete_contact(%s);", (del_id,))
            print(f"Контакт {del_id} удалён!")

        elif choice == "6":
            print("Выход...")
            break

        else:
            print("Некорректный выбор, попробуйте снова!")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()