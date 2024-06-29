ll = [input() for _ in range(3)]
result = 0
for i in range(3):
    if "Fizz" not in ll[i] and "Buzz" not in ll[i]:
        result = int(ll[i]) + 3 - i
        break

if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)
