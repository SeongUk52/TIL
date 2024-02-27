ll = list(input())
stack = 0
result = 0

for i in range(len(ll)):
    if ll[i] == "(":
        stack += 1
    else:
        if ll[i - 1] == "(":
            stack -= 1
            result += stack
        else:
            stack -= 1
            result += 1

print(result)
