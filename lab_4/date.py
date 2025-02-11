#task 1
from datetime import datetime, timedelta

current_date = datetime.today()

# Вычитаем 5 дней
new_date = current_date - timedelta(days=5)

print("Дата пять дней назад:", new_date.strftime("%Y-%m-%d"))

#task 2
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday.strftime("%Y-%m-%d"))
print("Сегодня:", today.strftime("%Y-%m-%d"))
print("Завтра:", tomorrow.strftime("%Y-%m-%d"))

#task 3
from datetime import datetime

now = datetime.now()

# Убираем микросекунды
without_microseconds = now.replace(microsecond=0)

print("Текущее время без микросекунд:", without_microseconds)

#task 4
from datetime import datetime

date1 = datetime(2024, 2, 1, 12, 0, 0)  # 1 февраля 2024, 12:00:00
date2 = datetime(2024, 2, 10, 14, 30, 0)  # 10 февраля 2024, 14:30:00

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Разница в секундах:", difference_in_seconds)

#also 4 
from datetime import datetime

def get_datetime_from_user(prompt):
    date_str = input(prompt + " (в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

# Запрашиваем у пользователя две даты
date1 = get_datetime_from_user("Введите первую дату и время")
date2 = get_datetime_from_user("Введите вторую дату и время")

# Вычисляем разницу в секундах
difference_in_seconds = abs((date2 - date1).total_seconds())

print("\nРазница в секундах:", difference_in_seconds)
