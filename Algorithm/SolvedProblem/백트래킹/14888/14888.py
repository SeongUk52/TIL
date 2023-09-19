def bt(n,A,op,comb,result):
    if len(comb) == n-1:
        sum = A[0]
        combs = comb[:]
        for i in range(1,n):
            oper = combs.pop(0)
            if oper == 0:
                sum += A[i]
            if oper == 1:
                sum -= A[i]
            if oper == 2:
                sum *= A[i]
            if oper == 3:
                if sum < 0:
                    sum = (-sum//A[i])*-1
                else:
                    sum //= A[i]
        result.append(sum)
    for i in range(4):
        if op[i]>0:
            op[i] -= 1
            comb.append(i)
            bt(n,A,op,comb,result)
            comb.pop()
            op[i] += 1

n = int(input())
A = list(map(int,input().split()))
op = list(map(int,input().split()))
result = []
bt(n,A,op,[],result)
print(int(max(result)))
print(int(min(result)))