def q1(l, r):
    cnt = 1
    for i in range(l - 1, r - 1):
        if s[i] != s[i + 1]:
            cnt += 1
    print(cnt)


def q2(l, r):
    for i in range(l - 1, r):
        if ord(s[i]) == 90:
            s[i] = 'A'
        else:
            s[i] = chr(ord(s[i]) + 1)


n, q = map(int, input().split())
s = list(input())
for i in range(q):
    q, l, r = map(int, input().split())
    if q == 1:
        q1(l, r)
    elif q == 2:
        q2(l, r)
