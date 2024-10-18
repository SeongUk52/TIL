k, s = map(int, input().split())
inputs = input()
result = ""
for i in inputs:
    if i.islower():
        result += chr(((ord(i) - 97) + k) % 26 + 97)
    elif i.isupper():
        result += chr(((ord(i) - 65) + k) % 26 + 65)
    else:
        result += i

print(result)
