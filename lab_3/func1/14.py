import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def is_palindrome(string):
    cleaned = ''.join(filter(str.isalnum, string)).lower()
    return cleaned == cleaned[::-1]

from func1 import sphere_volume, unique_elements, is_palindrome

print(sphere_volume(5))  # Вывод: 523.5987755982989
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Вывод: [1, 2, 3, 4, 5]
print(is_palindrome("racecar"))  # Вывод: True
