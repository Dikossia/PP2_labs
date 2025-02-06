def is_palindrome(string):
    cleaned = ''.join(filter(str.isalnum, string)).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))          # Вывод: True
print(is_palindrome("hello"))          # Вывод: False
print(is_palindrome("A man, a plan, a canal: Panama"))  # Вывод: True
