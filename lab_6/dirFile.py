#1 task

import os

def list_directories_and_files(path="."):
    print(f"\n📂 Список содержимого каталога: {path}\n")
    
    # Все элементы в директории
    all_items = os.listdir(path)
    
    # Фильтрация директорий
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
    
    # Фильтрация файлов
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    
    print("📁 Директории:", directories)
    print("📄 Файлы:", files)
    print("📦 Всё содержимое:", all_items)


list_directories_and_files(".")

#2 task

def check_access(path):
    print(f"\n🔍 Проверка доступа к пути: {path}")

    if os.path.exists(path):
        print("✅ Путь существует")
        print("📖 Доступ для чтения:", os.access(path, os.R_OK))
        print("✏ Доступ для записи:", os.access(path, os.W_OK))
        print("⚙ Доступ для выполнения:", os.access(path, os.X_OK))
    else:
        print("❌ Путь не существует")

check_access(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\example.txt")

#3 task

def check_path_info(path):
    if os.path.exists(path):
        print(f"\n📁 Путь '{path}' существует")
        print("📄 Имя файла:", os.path.basename(path))
        print("📂 Директория:", os.path.dirname(path))
    else:
        print(f"❌ Путь '{path}' не найден")

check_path_info(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\example.txt")

#4 task

def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(f"📖 Файл '{filename}' содержит {len(lines)} строк")
    except FileNotFoundError:
        print(f"❌ Файл '{filename}' не найден!")

count_lines(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\example.txt")

#5 task

def write_list_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            file.write(str(item) + "\n")
    print(f"✅ Список записан в файл '{filename}'")

data = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\languages.txt", data)

#6 task

import string

def create_alphabet_files():
    folder = "C:/Users/Huawei/Desktop/PP2_labs/alphabettxt"  # Папка, куда сохраняем файлы

    # Проверяем, существует ли папка, если нет – создаём
    if not os.path.exists(folder):
        os.makedirs(folder)

    for letter in string.ascii_uppercase:  # A-Z
        filename = os.path.join(folder, f"{letter}.txt")  # Формируем путь
        with open(filename, "w") as file:
            file.write(f"This is file {letter}.txt")  # Записываем в файл
        print(f"✅ Файл '{filename}' создан")

create_alphabet_files() 

#7 task

import shutil

def copy_file(source, destination):
    try:
        shutil.copyfile(source, destination)
        print(f"✅ Файл '{source}' скопирован в '{destination}'")
    except FileNotFoundError:
        print(f"❌ Файл '{source}' не найден!")

copy_file(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\example.txt", "copy_example.txt")

#8 task

import os

def delete_file(filename):
    if os.path.exists(filename):
        if os.access(filename, os.W_OK):
            os.remove(filename)
            print(f"✅ Файл '{filename}' удалён")
        else:
            print(f"❌ Нет прав на удаление '{filename}'")
    else:
        print(f"❌ Файл '{filename}' не найден")

delete_file(r"C:\Users\Huawei\Desktop\PP2_labs\lab_6\copy_example.txt")



