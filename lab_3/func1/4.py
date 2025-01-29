def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return list(filter(is_prime, numbers))

a = list(map(int, input().split()))
print(filter_prime(a)) 
