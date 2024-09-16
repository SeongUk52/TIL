N = int(input())
student_nums = []
for _ in range(N):
    student_nums.append(int(input()))
results = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        stu1 = student_nums[i]
        stu2 = student_nums[j]
        if stu1 == stu2:
            results[i] += 1
            results[j] += 1
        elif stu1 % stu2 == 0:
            results[i] += 1
        elif stu2 % stu1 == 0:
            results[j] += 1
for result in results:
    print(result)
