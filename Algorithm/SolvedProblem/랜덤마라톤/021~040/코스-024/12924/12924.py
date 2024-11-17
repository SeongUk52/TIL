a, b = map(int, input().split())
answer = 0

for i in range(a, b):
    str_i = str(i)
    length = len(str_i)
    seen = set()
    for l in range(1, length):
        rotated = int(str_i[-l:] + str_i[:-l])
        if i < rotated <= b and rotated not in seen:
            seen.add(rotated)
            answer += 1

print(answer)
