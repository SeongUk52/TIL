INF = 10**7
li = [1]*INF
for i in range(2, int(INF**0.5)+1):
    if li[i]:
        for j in range(i+i, INF, i):
            li[j] = 0
prime = [i for i in range(2, INF) if li[i]]
K = int(input())
print(prime[K-1])
