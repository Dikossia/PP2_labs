def print_even_numbers(numbers):
    """
    This function takes a list of numbers and prints the even ones.
    """
    for num in numbers:
        if num % 2 == 0:
            print(num)

# Example usage:
# numbers = [1, 2, 3, 4, 5, 6]
# print_even_numbers(numbers)