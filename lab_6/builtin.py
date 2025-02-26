#1 task 
import math

def multiply_list(numbers):
    return math.prod(numbers)  

# Пример
nums = [2, 3, 4, 5]
print("Произведение всех чисел:", multiply_list(nums))  

#1/2 
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print("Произведение всех чисел:", multiply_list([2, 3, 4, 5]))


#2 task
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    print(" Заглавных букв:", upper_count)
    print(" Строчных букв:", lower_count)

text = "Hello World! This is Python."
count_case(text)

#3 task
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()  # Убираем пробелы, делаем строчные буквы
    return cleaned == cleaned[::-1]  # Проверяем, равно ли слово своему зеркальному отображению

print(is_palindrome("Racecar"))  
print(is_palindrome("Python"))   
print(is_palindrome("A Santa Lived As a Devil At NASA"))  

import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Преобразуем миллисекунды в секунды
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

# Пример
num = 25100
delay = 2123  # 2123 мс
delayed_sqrt(num, delay)

#5 task
def all_true(t):
    return all(t)  # Проверяет, являются ли все элементы True

# Примеры
print(all_true((True, True, True)))  
print(all_true((True, False, True))) 
print(all_true((1, 2, 3)))           
print(all_true((0, 1, 2)))           

