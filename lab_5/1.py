a = input()
b = ""
for i in range(len(a)):
    if a[i] == "_":
        if i + 1 < len(a):
            b +=  a[i + 1].upper()
            i += 1
        else:
            continue
    else:
        if a[i - 1] == "_":
            continue
        else : b += a[i]

print(b)
