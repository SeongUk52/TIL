n = int(input())
if n > 0:
    print(len(bin(n))-2)
elif n < 0:
    print(32)
else:
    print(1)
