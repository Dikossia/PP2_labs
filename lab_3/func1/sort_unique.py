def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Вывод: [1, 2, 3, 4, 5]
