#task 1

import re 

a = r'^ab*$'
b = input().split() 

for i in b:
    if re.fullmatch(a, i):
        print("true")
    else: print("false")


#task 2

a = r'^ab{2,3}$'
b = input().split()

for i in b:
    if re.fullmatch(a, i):
        print("true")
    else: print("false")

#task 3

pattern = r'\b[a-z]+_[a-z]+\b'
text = input("Enter text: ")

matches = re.findall(pattern, text)
print("Matches:", matches)

#task 4

pattern = r'\b[A-Z][a-z]+\b'
text = input("Enter text: ")

matches = re.findall(pattern, text)
print("Matches:", matches)

#task 5

pattern = r'^a.*b$'
words = input("Enter words: ").split()

for word in words:
    print("true" if re.fullmatch(pattern, word) else "false")

#6 task

text = input("Enter text: ")
result = re.sub(r'[ ,.]', ':', text)

print("Modified text:", result)

#7 task

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

text = input("Enter snake_case string: ")
print("CamelCase:", snake_to_camel(text))

#8 task

text = input("Enter CamelCase string: ")
words = re.findall(r'[A-Z][a-z]*', text)

print("Words:", words)

#9 task

text = input("Enter CamelCase/PascalCase string: ")
result = re.sub(r'([A-Z])', r' \1', text).strip()

print("Modified text:", result)

#10 task

def camel_to_snake(camel_str):
    return re.sub(r'([A-Z])', r'_\1', camel_str).lower()

text = input("Enter camelCase string: ")
print("Snake case:", camel_to_snake(text))



