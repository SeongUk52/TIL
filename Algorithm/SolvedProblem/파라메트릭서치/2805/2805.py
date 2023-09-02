n, m = map(int,input().split())
trees = list(map(int,input().split()))
left,right = 0,max(trees)
while left<=right:
    mid = (left+right)//2
    total = sum([tree-mid for tree in trees if tree>mid])
    if total>=m:
        left = mid + 1
    else:
        right = mid - 1
print(right)