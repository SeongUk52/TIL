n = int(input())
ary = []

# 한 줄로 입력받아 처리
inputs = list(map(float, input().split()))

for k in inputs:
    mok = int(k)  # 정수 부분
    mod = 1 if k - mok > 0 else 0  # 소수점 여부 확인
    ary.append((mok, mod))

ans = ary[0][0] + ary[0][1]

for i in range(1, n):
    if ans == 0 and ary[i][1] == 1:
        ans += 1
    ans += ary[i][0]

print(ans)