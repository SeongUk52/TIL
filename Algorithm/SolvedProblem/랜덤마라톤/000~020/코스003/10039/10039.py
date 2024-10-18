ll = [int(input()) for _ in range(5)]
for i in range(5):
    if ll[i] < 40:
        ll[i] = 40
print(sum(ll) // 5)
