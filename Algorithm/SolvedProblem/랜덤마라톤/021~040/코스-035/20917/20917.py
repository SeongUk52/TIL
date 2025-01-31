import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    N,S=map(int,input().split())
    L=sorted(list(map(int,input().split())))
    start=1 ; end=max(L)
    while start<=end:
        mid=(start+end)//2
        left=L[0] ; count=1
        for i in range(1,N):
            right=L[i]
            if abs(right-left)>=mid:
                count+=1
                left=L[i]
        if count>=S:
            start=mid+1
        else:
            end=mid-1
    print(end)