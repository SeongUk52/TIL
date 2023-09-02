n = int(input())
ll = list(map(int,input().split()))
m = int(input())
if m >= sum(ll):
    print(max(ll))
else:
    left,right = 0,m
    while left<=right:
        mid = (left+right)//2
        result = sum([min(i,mid) for i in ll])
        if result>m:
            right = mid - 1
        else:
            left = mid + 1
    print(right)