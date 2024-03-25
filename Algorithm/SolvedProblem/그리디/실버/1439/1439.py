s = input()
temp = s[0]
cnt = 1
for i in s:
    if i != temp:
        temp = i
        cnt += 1
print(cnt // 2)
