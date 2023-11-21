from collections import deque
import sys
input = sys.stdin.readline

def main():
    p = deque(list(input()))
    n = int(input())
    x = deque(list(eval(input())))
    reverse_flag = False

    for y in p:
        if y == "D":
            if not x:
                print("error")
                return
            else:
                if reverse_flag:
                    x.pop()
                else:
                    x.popleft()
        elif y == "R":
            reverse_flag = not reverse_flag

    if reverse_flag:
        x.reverse()

    print('[', end='')
    print(*x, sep=',', end='')
    print(']')


tc = int(input())
for i in range(tc):
    main()
