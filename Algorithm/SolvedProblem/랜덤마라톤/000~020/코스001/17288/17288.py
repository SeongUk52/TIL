s = input()
cont = 1
result = 0

for i in range(len(s) - 1):
    if int(s[i + 1]) - int(s[i]) == 1:
        cont += 1
    else:
        if cont == 3:
            result += 1
        cont = 1
if cont == 3:
    result += 1
print(result)
