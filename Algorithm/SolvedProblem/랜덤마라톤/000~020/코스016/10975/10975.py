N = int(input())
nums = [int(input()) for _ in range(N)]
sortedNums = sorted(nums)
answer = 0
if N == 1:
    print(1)
    exit()
for i in range(N):
    for j in range(N):
        if nums[i] == sortedNums[j]:
            sortedNums[j] = 10000
            break
    if j == 0:
        if sortedNums[j + 1] != 10000:
            answer += 1
    elif j == N - 1:
        if sortedNums[j - 1] != 10000:
            answer += 1
    elif sortedNums[j - 1] == 10000 or sortedNums[j + 1] == 10000:
        continue
    else:
        answer += 1
print(answer)
