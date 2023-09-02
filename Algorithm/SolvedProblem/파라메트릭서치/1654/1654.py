k,n = map(int,input().split())
ll = [int(input()) for i in range(k)]
left,right = 0,max(ll)
while left<=right:
    mid = (left+right)//2
    if mid==0:  #제로 디비전 해소
        break
    ea = sum([i//mid for i in ll if i>=mid])
    if ea>=n:
        left = mid+1
    else:
        right = mid-1
print(right)