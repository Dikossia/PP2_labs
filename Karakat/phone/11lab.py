import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="karakat",  
    user="postgres",   
    password="dikossia06",  
    host="localhost",          
)

cursor = conn.cursor()

# Добавление или обновление одного контакта
def insert_or_update_user(user_name, numberph):
    try:
        cursor.execute("SELECT COUNT(*) FROM phonetry2 WHERE user_name = %s", (user_name,))
        count = cursor.fetchone()[0]

        if count > 0:
            cursor.execute("UPDATE phonetry2 SET numberph = %s WHERE user_name = %s", (numberph, user_name))
            print(f"Контакт {user_name} обновлён.")
        else:
            cursor.execute("INSERT INTO phonetry2 (user_name, numberph) VALUES (%s, %s)", (user_name, numberph))
            print(f"Контакт {user_name} добавлен.")

        conn.commit()
    except Exception as e:
        print(f"Ошибка при добавлении/обновлении контакта: {e}")
        conn.rollback()

# Поиск по шаблону
def search_by_pattern(pattern):
    try:
        cursor.execute(
            """
            SELECT user_id, user_name, numberph
            FROM phonetry2
            WHERE user_name LIKE %s OR CAST(numberph AS TEXT) LIKE %s
            ORDER BY user_id
            """,
            ('%' + pattern + '%', '%' + pattern + '%')
        )
        rows = cursor.fetchall()
        print("Найдено записей:", len(rows))
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")

# Удаление по имени
def delete_by_name(user_name):
    try:
        cursor.execute("DELETE FROM phonetry2 WHERE user_name = %s RETURNING *", (user_name,))
        deleted = cursor.fetchone()
        conn.commit()
        if deleted:
            print(f"Контакт {user_name} удалён.")
        else:
            print(f"Контакт {user_name} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")

# Удаление по номеру
def delete_by_phone(numberph):
    try:
        cursor.execute("DELETE FROM phonetry2 WHERE numberph = %s RETURNING *", (numberph,))
        deleted = cursor.fetchone()
        conn.commit()
        if deleted:
            print(f"Контакт с номером {numberph} удалён.")
        else:
            print(f"Контакт с номером {numberph} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")


# Вставка сразу нескольких контактов
def insert_multiple_users(data_list):
    for user_name, numberph in data_list:
        if len(numberph) > 10:
            print(f"❌ Неверный номер: {numberph} для {user_name}")
            continue

        cursor.execute("SELECT COUNT(*) FROM phonetry2 WHERE user_name = %s", (user_name,))
        exists = cursor.fetchone()[0]

        if exists:
            cursor.execute("UPDATE phonetry2 SET numberph = %s WHERE user_name = %s", (numberph, user_name))
        else:
            cursor.execute("INSERT INTO phonetry2 (user_name, numberph) VALUES (%s, %s)", (user_name, numberph))

    conn.commit()
    print("✅ Контакты добавлены или обновлены.")

# Показать с пагинацией
def get_contacts_with_pagination(limit, offset):
    try:
        cursor.execute("SELECT user_id, user_name, numberph FROM phonetry2 ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
        rows = cursor.fetchall()
        print("Найдено записей:", len(rows))
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")
    except Exception as e:
        print(f"Ошибка при получении контактов: {e}")

# Главное меню
if __name__ == '__main__':
    try:
        operation = input(
            "Выберите операцию:\n"
            "1 - Добавить или обновить контакт\n"
            "2 - Искать по шаблону\n"
            "3 - Удалить по имени\n"
            "4 - Удалить по номеру\n"
            "5 - Вставить несколько контактов\n"
            "6 - Показать контакты с пагинацией\n"
            "7 - найти номера где есть 707\n"


            "Ваш выбор: "
        )

        if operation == "1":
            name = input("Имя: ")
            phone = input("Телефон: ")  # Убираем проверку на 10 цифр
            insert_or_update_user(name, phone)

        elif operation == "2":
            pattern = input("Введите часть имени или номера: ")
            search_by_pattern(pattern)

        elif operation == "3":
            name = input("Имя для удаления: ")
            delete_by_name(name)

        elif operation == "4":
            phone = input("Номер для удаления: ")
            delete_by_phone(phone)

        elif operation == "5":
            count = int(input("Сколько контактов добавить: "))
            data = []
            for _ in range(count):
                name = input("Имя: ")
                phone = input("Телефон: ")  # Убираем проверку на 10 цифр
                data.append((name, phone))
            insert_multiple_users(data)

        elif operation == "6":
            limit = int(input("Сколько показать: "))
            offset = int(input("Сколько пропустить: "))
            get_contacts_with_pagination(limit, offset)

        elif operation == "7":
            cursor.execute("SELECT user_id, user_name, numberph FROM phonetry2 WHERE numberph LIKE '%707%'")
            rows = cursor.fetchall()
            print("Найдено записей:", len(rows))
            for row in rows:
                print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")
        

        else:
            print("Неверный ввод!")

    except Exception as e:
        print(f"Ошибка при выполнении операции: {e}")

    finally:
        cursor.close()
        conn.close()
