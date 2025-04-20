
        #elif operation == "7":
           # cursor.execute("SELECT user_id, user_name, numberph FROM phonetry2 WHERE numberph LIKE '+7%'")
           # rows = cursor.fetchall()
           # print("Найдено записей:", len(rows))
           # for row in rows:
               # print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")



       # elif operation == "7":
        #    cursor.execute("UPDATE phonetry2 SET numberph = REPLACE(numberph, '+7', '+8') WHERE numberph LIKE '+7%'")
         #   conn.commit()
           # print("Все номера с +7 заменены на +8.")

 # elif operation == "7":
  #          cursor.execute("SELECT user_id, user_name, numberph FROM phonetry2 WHERE numberph LIKE '%707%'")
    #        rows = cursor.fetchall()
     #       print("Найдено записей:", len(rows))
      #      for row in rows:
       #         print(f"ID: {row[0]}, Имя: {row[1]}, Номер: {row[2]}")




#вывести users score ascending 
#print("Топ игроков по счёту:")
#cursor.execute("SELECT user_name, score FROM users JOIN user_score ON users.user_id = user_score.user_id ORDER BY score DESC;")
#asc = cursor.fetchall()
#for row in asc:
   # print(f"Имя: {row[0]}, Счёт: {row[1]}")
# --- Выводим финальный счёт и уровень ---



asc = cursor.fetchall()
for row in asc:
    print(f"Имя: {row[0]}, Счёт: {row[1]}")