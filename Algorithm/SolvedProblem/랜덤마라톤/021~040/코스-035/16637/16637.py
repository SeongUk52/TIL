import sys

N = int(sys.stdin.readline())
cal = list(sys.stdin.readline().strip())
result = -2**31  # 최솟값

def calculate(a, op, b):
    return a + b if op == '+' else a * b if op == '*' else a - b

def dfs(index, value):
    global result
    if index >= N - 1:
        result = max(result, value)
        return

    dfs(index + 2, calculate(value, cal[index + 1], int(cal[index + 2])))

    if index + 4 < N:
        dfs(index + 4, calculate(value, cal[index + 1], calculate(int(cal[index+2]), cal[index+3], int(cal[index+4]))))

dfs(0, int(cal[0]))
print(result)