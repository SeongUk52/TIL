result = 0
n = int(input())

if n % 400 == 0:
    result = 1
elif n % 100 == 0:
    pass
elif n % 4 == 0:
    result = 1

print(result)
