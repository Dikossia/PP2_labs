import random
import string
import os
def random_filename():
    s = int(input())
    b = int(input())
    k = random.randint(s, b)  
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k)) + ".txt"

def createf(path):
    global last_file, d 
    d = 1
    last_file = random_filename()
    filr = os.path.join(path, last_file)
    
    with open(filr, "w") as f:
        f.write("random file", d)

    d +=1

def deletef(path):
    global last_file, d

    if not os.path.exists(path):
        return

    if last_file:
        last_path = os.path.join(path, last_file)
        if os.path.exists(last_path):
            os.remove(last_path)
            print(f" Deleted : {last_path}")
        else:
            print(f"thr file  {last_file} was not found.")

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if files:
        random_file = random.choice(files)
        os.remove(os.path.join(path, random_file))
        print(f"🗑 Удалён случайный файл: {random_file}")
    else: 
        print("Sorry.")

PATH = input("Введите путь к папке: ").strip()

if not os.path.exists(PATH):
    os.makedirs(PATH)  
    print(f"{PATH}")

while True:
    command = input().strip().lower()

    if command == "create":
        createf(PATH)
    elif command == "delete":
        deletef(PATH)
    elif command == "stop":
        print("Exiting...")
        break
    else:
        print("P;ease enter \"creatt\" , \"delete\" or \"stop\"")

