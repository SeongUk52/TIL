import sys

n = int(sys.stdin.readline())
gap = list(map(int,sys.stdin.readline().split()))
cities = list(map(int,sys.stdin.readline().split()))
total = 0
minimum = cities[0]
for i in range(n-1):
    if cities[i]<minimum:
        minimum = cities[i]
    total += minimum*gap[i]
print(total)