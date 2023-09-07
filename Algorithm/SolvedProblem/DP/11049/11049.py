import sys
input = sys.stdin.readline

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][-1]

n = int(input())
b=0
ms = []
for i in range(n):
    a,b = map(int,input().split())
    ms.append(a)
ms.append(b)

result = matrix_chain_order(ms)
print(result)
