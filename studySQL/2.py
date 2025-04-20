import psycopg2

conn = psycopg2.connect(
    dbname='for_study',
    user='postgres',
    password='dikossia06',
    host='localhost'
)
cursor = conn.cursor()


def insert_user(user_name, score):
    insert_query = """
    INSERT INTO users (user_name, score) 
    VALUES (%s, %s) RETURNING user_id, user_name, score;
    """
    cursor.execute(insert_query, (user_name, score))
    conn.commit()
    user_data = cursor.fetchone()
    print(f"Пользователь добавлен: ID = {user_data[0]}, Имя = {user_data[1]}, Баллы = {user_data[2]}")
    return user_data[0]  # Возвращаем ID нового пользователя

def list_to_CSV():
    select_query = "SELECT user_id, user_name, score FROM users ORDER BY score DESC;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("Пользователи, отсортированные по баллам (от максимального):")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Баллы: {row[2]}")

    with open('users.csv', 'a') as file:
        file.write("user_id,user_name,score\n")
        for row in rows:
            file.write(f"{row[0]},{row[1]},{row[2]}\n")



def update(num, user_name, score):
    if num == 1:
         update_query = """
            UPDATE users
            SET score = %s
            WHERE user_name = %s
            RETURNING user_id, user_name, score;
            """
    elif num == 2:
        update_query = """
            UPDATE users
            SET user_name = %s
            WHERE score = %s
            RETURNING user_id, user_name, score;
            """

    cursor.execute(update_query, (score, user_name))  # Здесь порядок параметров был неверен
    conn.commit()
    user_data = cursor.fetchone()

    if user_data:
        print(f"Данные обновлены: ID = {user_data[0]}, Имя = {user_data[1]}, Новые баллы = {user_data[2]}")
    else:
        if num == 1:
            print("Пользователь не найден.")
        elif num == 2:
            print("Номер не найден.")

def delete_user(user_name):   
    delete_query = """
    DELETE FROM users
    WHERE user_name = %s
    RETURNING user_id, user_name;
    """
    cursor.execute(delete_query, (user_name,))
    conn.commit()

    user_data = cursor.fetchone()

    if user_data:
        print(f"Пользователь удален: ID = {user_data[0]}, Имя = {user_data[1]}")
    else:
        print("Пользователь не найден.")

def get_all_users():
    select_query = "SELECT user_id, user_name, score FROM users;"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    print("Все пользователи:")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Баллы: {row[2]}")



def get_users_sorted_by_score():
    select_query = "SELECT user_id, user_name, score FROM users ORDER BY score DESC;"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    print("Пользователи, отсортированные по баллам (от максимального):")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Баллы: {row[2]}")

if __name__ == '__main__':
    operation = input("Choose\n1 - add users\n2 - update users\n3 - delete users\n4 - get all users\n5 - get users sorted by score\n")
    if operation == "1":
        name = input("Enter the name: ")
        score = int(input("Enter the score: "))  # Преобразуем score в int
        user_id = insert_user(name, score)  
        if user_id is not None:
            print("Contact successfully added. ID:", user_id)
        else:
            print("Error adding contact.")
    elif operation == "2":
        num = int(input("Enter 1 to update score or 2 to update name: "))  # Преобразуем num в int
        if num == 1:
            user_name = input("Enter the name of the contact you want to update: ")
            score = int(input("Enter the new score: "))  # Преобразуем score в int
            update(num, user_name, score)
        elif num == 2:
            score = int(input("Enter the score of the contact you want to update: "))  # Преобразуем score в int
            user_name = input("Enter the new name: ")
            update(num, user_name, score)
    elif operation == "3":
        name = input("Enter the name of the contact you want to delete: ")
        delete_user(name)
    elif operation == "4":
        get_all_users()
    elif operation == "5":
        get_users_sorted_by_score()
    elif operation == "6":
        list_to_CSV()

    # Закрытие соединения после выполнения всех операций
    cursor.close()
    conn.close()
