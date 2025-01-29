def reverse_words(sentence):
    words = sentence.split()  # Разделяем строку на слова
    return ' '.join(words[::-1])  # Переворачиваем порядок слов

print(reverse_words("We are ready"))  # Вывод: "ready are We"
