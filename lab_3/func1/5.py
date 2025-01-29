from itertools import permutations

def string_permutations(string):
    return [''.join(p) for p in permutations(string)]

s = input("Введите строку: ")
print(string_permutations(s))  