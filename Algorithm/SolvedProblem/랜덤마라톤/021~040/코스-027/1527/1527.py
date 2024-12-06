s, e = map(int, input().split())

def generate_lucky_numbers(limit, current, numbers):
    if int(current + '4') <= limit:
        numbers.append(current + '4')
        generate_lucky_numbers(limit, current + '4', numbers)
    if int(current + '7') <= limit:
        numbers.append(current + '7')
        generate_lucky_numbers(limit, current + '7', numbers)

total_s = []
total_e = []

generate_lucky_numbers(s - 1, '', total_s)
generate_lucky_numbers(e, '', total_e)

print(len(total_e) - len(total_s))