def isCanInstall(c,ll,mid):
    count = 1
    current_house = ll[0]

    for i in range(1, len(ll)):
        if ll[i] - current_house >= mid:
            count += 1
            current_house = ll[i]

    return count >= c

n,c = map(int,input().split())
ll = sorted([int(input()) for i in range(n)])
left,right = 1,ll[-1]-ll[0]
result = 0
while left<=right:
    mid = (left+right)//2
    if(isCanInstall(c,ll,mid)):
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)
