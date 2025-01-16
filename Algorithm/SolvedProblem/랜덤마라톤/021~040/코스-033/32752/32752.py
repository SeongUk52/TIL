def input_data():
    n, l, r = map(int, input().split())
    l -= 1
    a = list(map(int, input().split()))
    return n, l, r, a

def solve(n, l, r, a):
    a[l:r] = sorted(a[l:r])
    return all(a[i] <= a[i + 1] for i in range(n - 1))

n, l, r, a = input_data()
print(int(solve(n, l, r, a)))