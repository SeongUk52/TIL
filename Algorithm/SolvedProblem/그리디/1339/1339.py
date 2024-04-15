n = int(input())
words = {}
result = 0
for _ in range(n):
    word = list(input())
    for i in range(len(word)):
        if word[i] in words:
            words[word[i]] += 10 ** (len(word) - i - 1)
        else:
            words[word[i]] = 10 ** (len(word) - i - 1)

words = sorted(words.values())
cnt = 9
while words:
    result += words.pop() * cnt
    cnt -= 1

print(result)
