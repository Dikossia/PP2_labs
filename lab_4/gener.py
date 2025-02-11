#1/1 task

import math 

class MyNum:
    def __iter__(self):
        self.a = 1
        return self
    
    def get(self):
        self.N = int(input())

    def __next__(self):
        if self.a <= self.N:
            x = pow(self.a, 2)
            self.a += 1
            return x
        else:
            raise StopIteration
        
my_num = MyNum()
my_num.get()

for i in my_num:
    print(i)


#1/2 task
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2  # yild - возвращает значение и приостанавливает выполнение функции

N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")


#2/1 task
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0  # Start from 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.n:
            raise StopIteration  
        else:
            even_number = self.current
            self.current += 2  
            return str(even_number) 

n = int(input("Enter a number: "))

even_gen = EvenNumbers(n)

print(",".join(even_gen))

#2/2 task
def even_numbers(n):
    for i in range(0, n + 1, 2): 
        yield str(i)  

n = int(input("Enter a number: "))

print(",".join(even_numbers(n)))

#3/1 task
class By3_4:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:  
            if self.current % 3 == 0 and self.current % 4 == 0:
                result = self.current 
                self.current += 1 
                return str(result)  
            self.current += 1  
        
        raise StopIteration  

n = int(input("Enter a number: "))

by34 = By3_4(n)

print(" ".join(by34))

#3/2 task
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

for num in divisible_by_3_and_4(n):
    print(num, end=" ")

#4/1 task
class Squares:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.current = a  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.b:
            raise StopIteration  
        else:
            square = self.current ** 2  
            self.current += 1  
            return square 

a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))

squares_gen = Squares(a, b)

for square in squares_gen:
    print(square, end=" ")

#4/2 task
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))

for square in squares(a, b):
    print(square, end=" ")

#5/1 task
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current < 0:
            raise StopIteration 
        else:
            num = self.current 
            self.current -= 1  
            return num  

n = int(input("Enter a number: "))

countdown_gen = Countdown(n)

for num in countdown_gen:
    print(num, end=" ")

#5/2 task
def countdown(n):
    for i in range(n, -1, -1):  
        yield i

n = int(input("Enter a number: "))

for num in countdown(n):
    print(num, end=" ")




