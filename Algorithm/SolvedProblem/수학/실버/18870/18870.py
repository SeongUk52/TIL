n = int(input())
arr = list(map(int, input().split()))
sortedArr = sorted(set(arr))

dic = {sortedArr[i]: i for i in range(len(sortedArr))}

for i in arr:
    print(dic[i], end=" ")
