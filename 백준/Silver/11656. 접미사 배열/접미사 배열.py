word = input().strip()
result = []
for i in range(len(word)):
    suffix = ''.join(word[i:])
    result.append(word[i:])

result.sort()
for i in result:
    print(i)