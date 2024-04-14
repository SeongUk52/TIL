l, r = input().split()
cnt = 0
for i in range(len(r)):
    if len(r) != len(l):
        break
    if l[i] != r[i]:
        break
    if l[i] == '8' and r[i] == '8':
        cnt += 1

print(cnt)
