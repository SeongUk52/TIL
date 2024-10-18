answer = ""
for _ in range(int(input())):
    a, b, s = map(int, input().split())
    if s == 0:
        answer += "0 0\n"
        continue
    if a > s and b > s:
        answer += "Impossible\n"
        continue
    hi = max(a, b)
    lo = min(a, b)
    limit = int(s / hi)
    chk = False
    v = [False] * lo
    for i in range(limit, -1, -1):
        if chk:
            break
        remain = s - hi * i
        mod = remain % lo
        if v[mod]:
            chk = False
            break
        v[mod] = True
        if mod != 0:
            continue
        chk = True
        if hi == a:
            answer += str(i) + " " + str(remain // lo) + "\n"
        else:
            answer += str(remain // lo) + " " + str(i) + "\n"
    if not chk:
        answer += "Impossible\n"
print(answer)
