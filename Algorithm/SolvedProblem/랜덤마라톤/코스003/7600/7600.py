while True:
    inputs = input()
    if inputs == "#":
        break
    alphabet = set()
    for i in inputs:
        lower = i.lower()
        if 97 <= ord(lower) <= 122:
            alphabet.add(lower)
    print(len(alphabet))
