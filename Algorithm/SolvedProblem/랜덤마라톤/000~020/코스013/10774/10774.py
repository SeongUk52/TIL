j = int(input())
a = int(input())
jersey = [input() for _ in range(j)]
cnt = 0
for _ in range(a):
    size, num = input().split()
    num = int(num) - 1
    if jersey[num] != 'A':
        if size == 'S':
            jersey[num] = 'A'
            cnt += 1
        if size == 'M':
            if jersey[num] == 'M' or jersey[num] == 'L':
                jersey[num] = 'A'
                cnt += 1
        if size == 'L':
            if jersey[num] == 'L':
                jersey[num] = 'A'
                cnt += 1

print(cnt)
