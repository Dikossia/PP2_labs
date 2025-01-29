def spy_game(nums):
    code = [0, 0, 7]  # Код, который ищем
    for num in nums:
        if num == code[0]:  # Проверяем, совпадает ли текущий элемент с первым в коде
            code.pop(0)  # Убираем первый элемент кода
        if not code:  # Если код пуст, значит мы нашли последовательность
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Вывод: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Вывод: False
