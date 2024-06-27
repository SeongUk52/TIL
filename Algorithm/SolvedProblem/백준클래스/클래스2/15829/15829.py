result = 0
l = int(input())
ll = input()
for i in range(l):
    now = ord(ll[i]) - 96
    result += now * (31 ** i)
    result %= 1234567891
print(result)
