def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return "Решение не найдено"

a,b = int(input("Введите количество голов: ")), int(input("Введите количество ног: "))
print(solve(a,b))  
